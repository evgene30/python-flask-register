import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(body, filename, name, Division):
    def trans_lit(name_ones):
        conversion = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
                      'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
                      'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
                      'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': "i",
                      'ы': 'y', 'ь': "i", 'э': 'e', 'ю': 'ju', 'я': 'ja', ' ': ' '}
        key = ""
        for i in name_ones:
            try:
                i = conversion[i]
            except KeyError:
                alpha = "abcdefghijklmnopqrstuvwxyz"
                if i not in alpha:
                    i = "_"
            key += i
        return key

    foto_name_one = trans_lit(name)

    def MainMail(i):
        output_email = ''
        mail = {'Отдел декоративно-прикладного творчества и ИЗО': 'gavris-l@mail.ru',
                'Отдел спорта и туризма': 'minskopen@mail.ru',
                'Отдел интеллектуально-технического творчества': 'sv_3@bk.ru',
                'Отдел культурно-досуговой деятельности': 'orgtvor4@mail.ru',
                'Отдел социально-педагогической работы': 'psihologi_kontakt@mail.ru',
                'Отдел общественно-гуманитарной деятельности': 'dimoo.kontakt@mail.ru'
                }
        if i in mail:
            output_email = mail.get(i)

        else:
            print('Ошибка, данный адрес отсутвует')

        return output_email

    send_mail_name = MainMail(Division)

    subject = "Регистрация нового учащегося в электронной базе данных."  # тема письма
    sender_email = "minsk.kontakt@gmail.com"  # адрес отправителя
    receiver_email = send_mail_name  # адрес получателя
    password = "585858kontakt"

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

    foto_name = f"{foto_name_one}.jpeg"  # название картинки (латиница)
    print(foto_name_one)

    # Add header as key/value pair to attachment part
    part.add_header("Content-Disposition", f"attachment; filename= {foto_name}")

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context().verify = True
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
