from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class Registration(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	surname = StringField('Surname', validators=[DataRequired()])
	email = EmailField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
	confirm_password = PasswordField('Confirm password',
									 validators=[DataRequired(), Length(min=6), EqualTo('password')])
	submit = SubmitField('Submit registration')
