import subprocess
import json
import sys

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"[ERROR] {e.stderr.strip()}"

def get_first_running_pod(namespace):
    cmd = f"oc get pods -n {namespace} -o json"
    output = run_cmd(cmd)
    try:
        pods = json.loads(output)
        for pod in pods["items"]:
            if pod["status"]["phase"] == "Running":
                return pod["metadata"]["name"]
        return None
    except Exception:
        return None

def test_ping(pod, namespace, target):
    print(f"Testing ping to {target}...")
    cmd = f"oc exec -n {namespace} {pod} -- ping -c 3 {target}"
    output = run_cmd(cmd)
    return "PASS" if "0% packet loss" in output else f"FAIL: {output}"

def test_dns(pod, namespace, dns_name):
    print(f"Testing DNS resolution for {dns_name}...")
    cmd = f"oc exec -n {namespace} {pod} -- getent hosts {dns_name}"
    output = run_cmd(cmd)
    return "PASS" if dns_name in output else f"FAIL: {output}"

def test_internet(pod, namespace):
    print("Testing outbound internet access...")
    cmd = f"oc exec -n {namespace} {pod} -- curl -s --max-time 5 https://google.com"
    output = run_cmd(cmd)
    return "PASS" if "<title>Example Domain</title>" in output else f"FAIL: {output}"

def main():
    namespace = sys.argv[1] if len(sys.argv) > 1 else "default"
    print(f"\nChecking network from namespace: {namespace}")
    
    pod = get_first_running_pod(namespace)
    if not pod:
        print(f"[ERROR] No running pod found in namespace '{namespace}'")
        return

    print(f"Using pod: {pod}\n")

    results = {
        "Ping API Server": test_ping(pod, namespace, "example.com"),
        "DNS Resolution": test_dns(pod, namespace, "example.com"),
        "Internet Access": test_internet(pod, namespace)
    }

    print("\n Summary:")
    for test, result in results.items():
        print(f"{test}: {result}")

if __name__ == "__main__":
    main()

