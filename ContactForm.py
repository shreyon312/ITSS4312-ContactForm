from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email
from wtforms import widgets

class ContactForm(FlaskForm):
    email = EmailField("Enter your email:", validators=[DataRequired(), Email()])
    rating = RadioField("Rate your experience!", choices=[(5, '★'),(4,'★'),(3,'★'),(2,'★'),(1,'★')])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit Feedback")

