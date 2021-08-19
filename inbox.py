from email import message
import imaplib
import email


def get_emails():
    mail = imaplib.IMAP4_SSL(host="imap.gmail.com")
    mail.login(user="japytubechannel@gmail.com",
               password="0994191243rimy@@@rimy94")
    mail.select("inbox")
    _, search_data = mail.search(None, "ALL")
    messages = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        my_data = email.message_from_bytes(b)
        for header in ['subject', 'from', 'to', 'date']:
            print("{}: {}".format(header, my_data[header]))
            email_data[header] = my_data[header]
        for part in my_data.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == 'text/html':
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        messages.append(email_data)
        for msg in messages:
            m = """
            {}:{}
            {}:{}
            {}:{}
            {}:{}
            {}:{}
                """.format('subject', msg['subject'], 'from', msg['from'], 'to', msg['to'], 'date', msg['date'], 'body', msg['body'])
            print(m)
            print('=============================')
    mail.close()
    mail.logout()


if __name__ == "__main__":
    get_emails()
