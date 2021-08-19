from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
from typing import TypedDict
username = "japytubechannel@gmail.com"
password = "0994191243rimy@@@rimy94"
htm = """
    <h1> please find my attachment</h1>
    <img src="cid:img1">
        """


def send_email(email_from="Japy Tube <japytubechannel@gmail.com>", email_to=None, subject="Don't reply", text="email body", html=htm):
    my_msg = MIMEMultipart("related")
    my_msg["From"] = email_from
    my_msg["To"] = email_to
    my_msg["Subject"] = subject
    my_html = MIMEText(html, "html")
    my_msg.attach(my_html)
    my_img = open("ahmed.jpg", "rb")
    my_o_img = MIMEImage(my_img.read())
    my_img.close()
    my_o_img.add_header("Content-ID", "<img1>")

    my_msg.attach(my_o_img)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(email_from, email_to, my_msg.as_string())
