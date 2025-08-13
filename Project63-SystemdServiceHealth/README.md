## Scenario 63: Systemd Service Health & Auto-Restarter  
**Problem Statement: In production Linux servers, critical services (like nginx, postgresql, or custom apps) may fail or crash unexpectedly. Manual restarts take time and can lead to downtime.**  

**Detailed Scenario: An SRE team needs a lightweight Python tool that periodically checks the status of defined systemd services. If any service is found inactive, the tool should log event, Restart service automatically.**  

**Use Case Approach: Read the list of critical services from a configuration file, If the service is inactive, restart it and log the event.**  

**Tools and Modules: subprocess, **  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Read the list of critical services from a configuration file  
- Use subprocess to run systemctl is-active <service>  
- If the service is inactive, restart it and log the event  
- Optionally integrate with SMTP or Slack Webhooks for alerts  
- Support both one-time check and continuous monitoring modes  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

# Run one-time check
python service_health_checker.py services.txt --once

# Monitor continuously every 60 seconds
python service_health_checker.py services.txt --interval 60
