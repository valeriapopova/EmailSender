from email.mime.multipart import MIMEMultipart
from email.utils import make_msgid

from flask import Flask, request, Response
import smtplib
from werkzeug.exceptions import BadRequestKeyError

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

login = '@mail.ru'
passwd = ''


@app.route('/email/post', methods=['POST', 'GET'])
def post_email():
    if request.method == 'POST':
        try:
            json_file = request.get_json(force=False)
            name = json_file['data'][0]['name']
            phone = json_file['data'][1]['phone']
            to = json_file['to']
            try:
                msg = MIMEMultipart()
                msg['Message-ID'] = make_msgid()
                msg['Subject'] = f'Новый лид!!! имя {name} , номер телефона {phone}'
                msg['From'] = login
                msg['To'] = to
                s = smtplib.SMTP_SSL("smtp.mail.ru", 465)
                s.login(login, passwd)
                s.sendmail(login, to, msg.as_string())
                s.quit()
                return Response("Сообщение отправлено", 201)
            except:
                Response("Сообщение  не отправлено", 404)

        except BadRequestKeyError:
            return Response("Пустое значение", 400)

