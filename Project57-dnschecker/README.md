## Scenario 57: DNS Health & Resolution Checker
**Problem Statement: Ensure that critical domains (e.g., APIs, internal tools, external services) resolve correctly and are not experiencing DNS issues.**  

**Detailed Scenario: SREs often depend on DNS working correctly for service availability. A DNS health checker script can verify domain resolution, TTL, and optionally check propagation across public resolvers (Google, Cloudflare, etc.).**  

**Use Case Approach: Read list of domains from a file, Check A/AAAA, CNAME, TTL value, and response time, Optionally compare resolution from different DNS servers**  

**Tools and Modules: dnspython, argparse, logging, csv**  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Read list of domains from a file.  
- Check A/AAAA, CNAME, TTL value, and response time.  
- Optionally compare resolution from different DNS servers.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════


