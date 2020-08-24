import smtplib, ssl


def send_mail(message):
    port = 465 # порт
    smtp_server = 'smtp.mail.ru' # почтвый сервер
    sender_email = 'sv_3@bk.ru'  # адрес отправителя, логин
    receiver_email = 'sv_3@bk.ru'  # кому
    password = '1487'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# send_mail(message="""Subject: Hi there.This message is sent from Python.""") #file='/home/pavel/Изображения/2019/03/15/DSC_0028.jpg')
