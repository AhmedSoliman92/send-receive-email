import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
username = 'japytubechannel@gmail.com'
password = '0994191243rimy@@@rimy94'


def send_email(text='Email Body', subject='Hello world', from_email='Japy Tube <japytubechannel@gmail.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.ehlo()
        server.starttls()
        server.login(user=username, password=password)
        server.sendmail(from_email, to_emails, msg_str)
