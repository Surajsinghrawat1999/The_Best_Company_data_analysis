import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "surajsinghrawat1999@gmail.com"
    password = "oqjdiklfspfvsmhz"
    reciever = "surajsinghrawat1999@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)