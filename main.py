from flask import Flask, render_template, request, redirect, url_for

from flask_wtf import FlaskForm

from flask_bootstrap import Bootstrap5

# import flask_bootstrap
from wtforms import StringField, SubmitField
import smtplib

my_email = "lindokuhlemotha275@gmail.com"
my_password = "lxjehwnzbzgtesec"

friend_email = "civilmotha@gmail.com"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Contact_Us(FlaskForm):
    name = StringField('Your name')
    email = StringField('Email')
    message = StringField('Message')
    send = SubmitField('Ok')



# db = SQLAlchemy()




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact',  methods=['GET', 'POST'])
def contact():
    form = Contact_Us()
    if request.method == 'POST':
        if form.validate_on_submit:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=friend_email,
                                    msg=f"Message{form.message}\nFrom: {form.name}\n Email: {form.email}")
                connection.close()
            print("worked")
            return redirect(url_for('home'))
    return render_template('contact.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/works')
def works():
    return render_template('works.html')







if __name__ == "__main__":
    app.run(debug=True)

