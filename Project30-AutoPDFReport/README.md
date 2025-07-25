## Scenario 30: Automating Report Generation  
**Problem Statement: Automatically generating and sending PDF reports.**  

**Detailed Scenario: A system needs to generate PDF reports from dynamic data and send them via email at specific intervals.**  

**Usecase Approach: Use Python’s reportlab module to generate PDFs and smtplib to send emails.**  

**Tools and Modules: reportlab, smtplib**  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════  
Approach:  
- Use reportlab to design a structured, readable PDF  
- Fetch real-time OpenStack VM data (dummy in example)  
- Use smtplib to securely send the email with PDF attached  
- Can be scheduled using cron or schedule Python module  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════


We can add this function and incorporate to fetch the latest data from OpenStack itself.


```
def fetch_openstack_vms():
    conn = connection.Connection(
        auth_url=os.getenv("OS_AUTH_URL"),
        project_name=os.getenv("OS_PROJECT_NAME"),
        username=os.getenv("OS_USERNAME"),
        password=os.getenv("OS_PASSWORD"),
        user_domain_name=os.getenv("OS_USER_DOMAIN_NAME", "default"),
        project_domain_name=os.getenv("OS_PROJECT_DOMAIN_NAME", "default")
    )

    vm_list = []
    for server in conn.compute.servers():
        vm_info = {
            "Name": server.name,
            "Status": server.status,
            "IP": next(iter(server.addresses.values()))[0]['addr'] if server.addresses else "N/A"
        }
        vm_list.append(vm_info)
    return vm_list
```

<img width="572" height="440" alt="image" src="https://github.com/user-attachments/assets/9ca6dd12-3cf4-4005-9e67-f64ec5f6256d" />
