import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(body,filename):
    subject = "Регистрация нового учащегося в электронной базе данных."  # тема письма
    #body = "This is an email with attachment sent from Python" # сообщение
    #filename = 'D:/Мои рисунки/IMG_0465.jpg' # файл
    sender_email = "sv_3@bk.ru"  # адрес отправителя
    receiver_email = "sv_3@bk.ru"  # адрес получателя
    password = '1487'



    # Создание заголовка(компиляция) письма при помощи MIMEMultipart
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # добавление письма в тело документа
    message.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    foto_name = 'IMG.jpg' # название картинки
    # Add header as key/value pair to attachment part
    part.add_header("Content-Disposition", f"attachment; filename= {foto_name}")

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.mail.ru", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

