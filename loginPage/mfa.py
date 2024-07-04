import random
from email.message import EmailMessage
import ssl
import smtplib

def emailSender():
    code = random.randint(1000, 9999)
    email_sender = 'REMOVED'
    email_password ='REMOVED'
    email_reciever = 'REMOVED'

    subject = 'hello world'

    string = str(code)

    body = """
    Here is your password
     """ + string


    # elements of email
    em = EmailMessage()
    em['From'] = email_sender
    em['to'] = email_reciever
    em ['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    # sending email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

        return string


num = emailSender()
print(num)



