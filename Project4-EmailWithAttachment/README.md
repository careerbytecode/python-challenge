## Scenario 4: Sending Automated Emails with Attachments

**Problem Statement:**  
Send an automated email with a report attached.

**Detailed Scenario:**  
The system generates a daily report, which should be sent automatically to a list of recipients, including as an attachment.

**Use Case Approach:**  
Use the `smtplib` module to send emails and attach reports generated via Python.

**Tools and Modules:**  
`smtplib`, `email`, `os`

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

**Approach:**  

- Export email and password to environment variables  
- Provide recipient, subject, email body, and attachment  
- Open the file and read the data  
- Verify if the attachment exists; otherwise, return an error  
- Send the email or return an error if unsuccessful  

**Python Modules Used:**  

- `os`: For file system-level operations  
- `smtplib`: A built-in Python module that allows you to send emails using the SMTP protocol  
- `EmailMessage`: The `EmailMessage` class (from the `email.message` module) is used to create and manage email messages in a clean, structured, and modern way  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

I have implemented similar scripts in various automation scenarios, setting up both scheduled and on-demand tasks for handling outgoing and incoming emails. 
In one automation, an email sent from a mobile device or web browser included a secret code and arguments in the subject line. When the email arrived at a designated Linux server, it triggered a script that parsed the subject and body for instructions, generated the requested report, and sent it to the specified recipients. The process incorporated multiple security checks, such as verifying the sender against an authorized user list, validating code combinations, and inspecting email headers before executing any actions.

I have used email aliases like this:
use `/etc/aliases` to pipe email directly to a program for processing. For example, to run a script to process all email sent to `test@domain.com`, add this line to `/etc/aliases` (works for Postfix, Sendmail, etc.):

```
test:              "|/usr/local/bin/processtestemail.php"
```
══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

**References:**  
- https://docs.python.org/3/library/email.message.html#email.message.EmailMessage  
- https://docs.python.org/3/library/smtplib.html  
- https://serverfault.com/questions/506894/how-to-route-email-to-a-script  
