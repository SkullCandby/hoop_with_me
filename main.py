from flask import Flask, render_template, request
from flask_mail import Mail, Message
from random import randint
import random
from email.message import EmailMessage
import ssl
import smtplib
import re
app = Flask(__name__, template_folder='C:/Users/dvmes/PycharmProjects/hoop with me/template')
mail = Mail(app)

email_sender = 'gdmeshkov@gmail.com'
email_password = 'leaDer2012'
email_rec = 'gdmeshkov@mail.ru'
subject = 'ayo!! check this out '
otp = None

pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"


def test_email(your_pattern, email):
    pattern = re.compile(your_pattern)
    emails = [email]
    for email in emails:
        if not re.match(pattern, email):
            return False
        else:
            return True


@app.route('/', methods=["GET"])
def index():
    return render_template("register.html")


@app.route('/', methods=["POST"])
def index_():
    print(request.form.get('email'), 1)
    if request.form.get('submit_email') is not None:
        global otp
        global pattern
        if test_email(pattern, request.form.get('email')):
            otmp = str(random.randint(100000, 999999))
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = request.form.get('email')
            em['Subject'] = subject
            em.set_content(otmp)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
                smpt.login(email_sender, 'cfwsvisgwztlsewk')
                smpt.sendmail(email_sender, email_rec, em.as_string())
            otp = otmp

    return render_template("register.html")

@app.route('/verify', methods=["POST"])
def verify():

    return render_template('verify.html')


@app.route('/validate', methods=['POST'])
def validate():
    global otp
    user_otp = request.form['otp']
    print(type(otp), type(user_otp))
    if int(otp) == int(user_otp):
        return "<h3>Email varification succesfull</h3>"
    return "<h3>Please Try Again</h3>"


if __name__ == '__main__':
    app.run()
