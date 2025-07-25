from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from email.message import EmailMessage
import smtplib
import os

def generate_pdf(filename="openstack_report.pdf", data=None):
    if data is None:
        data = [
            {"Name": "vm01", "Status": "ACTIVE", "IP": "10.0.0.1"},
            {"Name": "vm02", "Status": "SHUTOFF", "IP": "10.0.0.2"},
            {"Name": "vm03", "Status": "ACTIVE", "IP": "10.0.0.3"},
            {"Name": "vm04", "Status": "SHUTOFF", "IP": "10.0.0.4"},
            {"Name": "vm05", "Status": "SHUTOFF", "IP": "10.0.0.5"},
            {"Name": "vm06", "Status": "ACTIVE", "IP": "10.0.0.6"},
            {"Name": "vm07", "Status": "ACTIVE", "IP": "10.0.0.7"},
            {"Name": "vm08", "Status": "SHUTOFF", "IP": "10.0.0.8"},
            {"Name": "vm09", "Status": "ACTIVE", "IP": "10.0.0.9"},
        ]

    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 750, "OpenStack Report")
    c.setFont("Helvetica", 12)

    y = 720
    for vm in data:
        line = f"Name: {vm['Name']} | Status: {vm['Status']} | IP: {vm['IP']}"
        c.drawString(50, y, line)
        y -= 20

    c.save()
    return filename

def send_email_with_attachment(sender, receiver, password, subject, body, file_path):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="pdf",
                filename=os.path.basename(file_path)
            )
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    pdf_path = generate_pdf()

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("EMAIL_PASSWORD")

    send_email_with_attachment(
        sender=EMAIL or "email@gmail.com",
        receiver="recipient@example.com",
        password=PASSWORD or "email_password",
        subject="Automated OpenStack Report",
        body="Attached is the latest OpenStack VM report.",
        file_path=pdf_path
    )

