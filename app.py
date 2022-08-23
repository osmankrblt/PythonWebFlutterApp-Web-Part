from flask import Flask, render_template, url_for, request, flash
from Helper.firestoreHelper import FirebaseHelper
import time
firebaseHelper = FirebaseHelper()

app = Flask(__name__, static_folder='D:\Python Project\Web Project\Django Projesi\PythonWebFlutterApp\static',)
app.debug = True
app.secret_key = 'super secret key'


@app.route('/',methods=['GET', 'POST'])
def contact():  # put application's code here

    if request.method == 'POST':

        user = " ".join([request.form.get('name') , request.form.get('surname')])
        #user += time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        durum = firebaseHelper.addData(name=user,mail=email,title=subject,content=message)
        flash("Notunuz iletildi...",category="success") if durum else flash("Notunuz iletilemedi.FirebaseHatası...",category="error")

        return render_template("index.html")

    else:
        return render_template("index.html")


if __name__ == '__main__':

    app.run()
