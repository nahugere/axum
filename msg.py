import smtplib
import os

username = os.environ.get('DEV_EMAIL')

class EmailMessager:

    def __init__(self):
        pass

    def sendEmail(self, reciever, serial_key):

        username = os.environ.get('DEV_EMAIL')
        password = os.environ.get('DEV_EMAIL_PASSWORD')

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(username, password)

            subject = 'Serial key'
            body = f'{serial_key}'

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(username, reciever, msg)
