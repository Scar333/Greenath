from mail import password, sender_log
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def send_mail(size):
    sender = sender_log
    pass_word = password

    # Подключение
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:     
        xlsxfile = 'New.xlsx'

        server.login(sender, pass_word)
        msg = MIMEMultipart()
    
        msg["Subject"] = 'Высылаю таблицу'
            
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(xlsxfile, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'%(xlsxfile))
        msg.attach(part)

        text = "Количество строк : " + str(size)
        msg.attach(MIMEText(text))


        server.sendmail(sender, sender, msg.as_string())
        server.quit()

        return 'Message send!'
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password!"