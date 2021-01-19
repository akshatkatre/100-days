import smtplib
from common import resource


def send_email(email_subject: str, message_body: str):
    SENDER_EMAIL = resource.get_resource_key("email")["user"]
    PASSWORD = resource.get_resource_key("email")["pass"]
    to_email_address = resource.get_resource_key("email")["recepient"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=to_email_address,
            msg=f"subject:{email_subject}\n\n{message_body}"
        )