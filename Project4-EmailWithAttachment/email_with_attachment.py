import os
import smtplib
from email.message import EmailMessage

# Set environment variables:
# export EMAIL_USER="your-email@gmail.com"
# export EMAIL_PASS="your-app-password"

SENDER_EMAIL = os.environ.get("EMAIL_USER")
SENDER_PASSWORD = os.environ.get("EMAIL_PASS")

RECIPIENTS = ["recipient1@gmail.com", "recipient2@gmail.com"]
SUBJECT = "Daily Report"
BODY = (
    "Hi Team,\n\n"
    "Please find attached the daily report.\n\n"
    "Regards,\nAutomation Team"
)
ATTACHMENT_PATH = "daily_report.csv"

def send_email_with_attachment():
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Email credentials not set in environment variables.")
        return

    if not os.path.exists(ATTACHMENT_PATH):
        print(f"File not found: {ATTACHMENT_PATH}")
        return

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = SUBJECT
    msg.set_content(BODY)

    with open(ATTACHMENT_PATH, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(ATTACHMENT_PATH)
        )

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_email_with_attachment()
