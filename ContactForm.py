from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    # name = StringField("Name")
    email = EmailField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message")
    submit = SubmitField("Submit")

