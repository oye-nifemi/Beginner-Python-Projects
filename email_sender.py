from email.message import EmailMessage
import ssl
import smtplib

email_sender = "xinix.0000@gmail.com"
email_password = "hjhnrnrezappnqqy"

email_reciever = "nifoyewole@gmail.com"

subject = "Learning"
body = """
Hey there, I trust that you are doing fine.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())