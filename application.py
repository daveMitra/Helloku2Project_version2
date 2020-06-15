from flask import Flask, render_template
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='mail.ad.ge.com',
    MAIL_PORT=25,
    # MAIL_USE_SSL=True,
    MAIL_USERNAME='MyTech.Software@ge.com',
    # MAIL_PASSWORD='Uipath@8732'
    # EMAIL SETTINGS
    # MAIL_SERVER='mail.ad.ge.com',
    # MAIL_PORT=25,
    # # MAIL_USE_SSL=True,
    # MAIL_USERNAME='MyTech.Software@ge.com',
    # MAIL_PASSWORD='Uipath@8732'
)
mail = Mail(app)


@app.route('/')
def mailSend():
    try:
        msg = Message("Send Mail Tutorial!",
                      sender="MyTech.Software@ge.com",
                      recipients=["Debartha.Mitra@ge.com"])
        # msg.body = "Yo!\nHave you heard the good word of Python???"
        # msg.html = render_template('text.html')
        msg.html = render_template('linkPage.html')
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        print(type(e))
        print(e)
        return 'error'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)