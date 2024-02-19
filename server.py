from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

import smtplib

my_email = "lindokuhlemotha275@gmail.com"
my_password = "CivilMotha94"

friend_email = "civilmotha@gmail.com"


# app = Flask(__name__)
#
# class Contact_Us(FlaskForm):
#     name = StringField('Your name')
#     email = StringField('Your Review')



# db = SQLAlchemy(



#
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/contact',  methods=['GET', 'POST'])
# def contact():
#     form = Contact_Us()
#     return render_template('contact.html', form=form)



# if __name__ == "__main__":
#     app.run(debug=True)

with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=friend_email,
                                    msg='Yaay')
            connection.close()
            print("worked")

