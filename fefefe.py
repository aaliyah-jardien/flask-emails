from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aaliyahjar13@gmail.com'
app.config['MAIL_PASSWORD'] = 'icecream2002%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/', methods=['POST'])
def index():
    response = {}
    if request.method == 'POST':
        msg = Message('Hello Message', sender='aaliyahjar13@gmail.com', recipients=['zaidflandorp4@gmail.com'])
        msg.body = "This is the email body after making some changes"
        mail.send(msg)
        response['message'] = "Send email"
        response['status_code'] = 201

    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
