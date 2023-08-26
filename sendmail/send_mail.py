import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, message, from_email, to_email, password):
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    from_email = 'mrdunghr@gmail.com'
    app_password = 'zcnkuptsmslbdujc'

    to_email = 'mrdunghr@gmail.com'
    subject = 'Hello from Python!'
    message = 'This is a test email sent from a Python script.'

    send_email(subject, message, from_email, to_email, app_password)
