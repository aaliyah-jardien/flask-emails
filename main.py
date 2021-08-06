# import Mail & Message from flask_mail
from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)

# CONFIGURE SERVER PARAMETERS
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aaliyahjar13@gmail.com'
app.config['MAIL_PASSWORD'] = 'icecream2002%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def index():
    mail = Mail(app)
    msg = Message('Hello Message', sender='aaliyahjar13@gmail.com', recipients=['zaidflandorp4@gmail.com'])
    msg.body = "My email using Flask"
    mail.send(msg)
    return "Message send"

if __name__ == '_main_':
    app.debug = True
    app.run()
