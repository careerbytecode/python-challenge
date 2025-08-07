import dns.resolver
import argparse
import logging
from datetime import datetime

logging.basicConfig(
    filename='dns_check.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_dns(domain, nameservers=None):
    resolver = dns.resolver.Resolver()
    if nameservers:
        resolver.nameservers = nameservers

    try:
        answer = resolver.resolve(domain, 'A')
        ips = [rdata.address for rdata in answer]
        ttl = answer.rrset.ttl
        return {"domain": domain, "ips": ips, "ttl": ttl, "status": "OK"}
    except Exception as e:
        logging.error(f"Error resolving {domain}: {e}")
        return {"domain": domain, "ips": [], "ttl": None, "status": f"ERROR: {e}"}

def main():
    parser = argparse.ArgumentParser(description="DNS Health & Resolution Checker")
    parser.add_argument("domain", help="Domain name to check")
    parser.add_argument("--nameservers", nargs="*", help="Optional custom DNS servers (e.g., 8.8.8.8 1.1.1.1)")
    args = parser.parse_args()

    print(f"Checking DNS for: {args.domain}")
    results = check_dns(args.domain, args.nameservers)

    print("\nDNS Report:")
    print(f"Domain     : {results['domain']}")
    print(f"Status     : {results['status']}")
    print(f"IP(s)      : {', '.join(results['ips']) if results['ips'] else 'N/A'}")
    print(f"TTL        : {results['ttl'] if results['ttl'] else 'N/A'}")

    logging.info(f"Checked {args.domain} - Status: {results['status']} - IPs: {results['ips']}")

if __name__ == "__main__":
    main()

