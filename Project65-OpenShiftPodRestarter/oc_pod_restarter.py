#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from typing import List, Dict, Tuple, Optional

BAD_REASONS = {
    "CrashLoopBackOff",
    "ImagePullBackOff",
    "ErrImagePull",
    "RunContainerError",
    "CreateContainerError",
    "ContainerCannotRun",
}

def log(msg: str, error: bool = False) -> None:
    print(msg, file=sys.stderr if error else sys.stdout)

def run_cmd(cmd: List[str]) -> Tuple[int, str, str]:
    try:
        result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        log("Error: 'oc' command not found. Please install OpenShift CLI and ensure it's in PATH.", error=True)
        sys.exit(2)

def get_pods_json(namespace: Optional[str], selector: Optional[str]) -> Dict:
    cmd = ["oc", "get", "pods", "-o", "json"]
    cmd += ["-n", namespace] if namespace else ["-A"]
    if selector:
        cmd += ["-l", selector]

    rc, out, err = run_cmd(cmd)
    if rc != 0:
        log(f"Command failed: {' '.join(cmd)}\n{err or out}", error=True)
        sys.exit(1)

    try:
        return json.loads(out)
    except json.JSONDecodeError:
        log("Error: Failed to parse JSON from 'oc' output.", error=True)
        sys.exit(1)

def pod_unhealthy_info(pod: Dict) -> Optional[str]:
    status = pod.get("status", {})
    phase = status.get("phase")
    reason = status.get("reason")

    if phase in {"Failed", "Unknown"}:
        return f"phase={phase} reason={reason or 'n/a'}"

    for field in ("containerStatuses", "initContainerStatuses"):
        for cs in status.get(field, []) or []:
            state = cs.get("state", {})
            if waiting := state.get("waiting"):
                w_reason = waiting.get("reason")
                if w_reason in BAD_REASONS:
                    return f"{field}:{cs.get('name')} waiting={w_reason}"
            if terminated := state.get("terminated"):
                t_reason = terminated.get("reason")
                if t_reason and t_reason not in {"Completed", "Succeeded"}:
                    return f"{field}:{cs.get('name')} terminated={t_reason}"

    msg = status.get("message", "")
    if isinstance(msg, str) and "CrashLoopBackOff" in msg:
        return "CrashLoopBackOff (message)"

    return None

def delete_pod(namespace: str, name: str, dry_run: bool) -> bool:
    cmd = ["oc", "delete", "pod", name, "-n", namespace, "--ignore-not-found=true"]
    if dry_run:
        log(f"DRY-RUN: {' '.join(cmd)}")
        return True

    rc, out, err = run_cmd(cmd)
    if rc == 0:
        log(f"Deleted pod {namespace}/{name} -> controller will recreate")
        return True
    else:
        log(f"Failed to delete pod {namespace}/{name}\n{err or out}", error=True)
        return False

def main():
    parser = argparse.ArgumentParser(description="OpenShift Pod Restarter (find bad pods and restart them)")
    parser.add_argument("-n", "--namespace", help="Namespace to scan (default: all namespaces)")
    parser.add_argument("--selector", help="Label selector (e.g., app=myapp)")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without deleting pods")
    args = parser.parse_args()

    pods = get_pods_json(args.namespace, args.selector).get("items", [])
    scope = args.namespace or "ALL namespaces"
    if not pods:
        log(f"No pods found in {scope} (selector: {args.selector or 'none'}).")
        return

    log(f"Scanning {len(pods)} pod(s) in {scope} {f'(selector: {args.selector})' if args.selector else ''}")

    unhealthy = [
        (pod["metadata"]["namespace"], pod["metadata"]["name"], info)
        for pod in pods
        if (info := pod_unhealthy_info(pod))
    ]

    if not unhealthy:
        log("No unhealthy pods detected.")
        return

    log(f"Found {len(unhealthy)} unhealthy pod(s):")
    for ns, name, info in unhealthy:
        log(f" - {ns}/{name}: {info}")
        delete_pod(ns, name, args.dry_run)

    log("\nDRY-RUN complete. No pods were deleted." if args.dry_run else
        "\nDone. If these pods are managed by a controller, they should be recreated automatically.")

if __name__ == "__main__":
    main()

