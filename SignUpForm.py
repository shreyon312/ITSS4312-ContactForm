from flask_wtf import Form
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, TextAreaField

class RegistrationForm(Form):
    name = StringField("Candidate Name ", [validators.DataRequired()])
    email = StringField("Email Address", [validators.DataRequired()])
    Address = TextAreaField("Address")
    password = PasswordField("New Password", [validators.DataRequired()])
    signin = SubmitField("Sign up")