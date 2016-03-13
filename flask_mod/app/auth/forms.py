from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, NoneOf
from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(Form):
    email = StringField('Enter your Email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Enter your password', validators=[DataRequired(),
                                            EqualTo('password2', message='Passwords must be match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    UserName = StringField('Enter your UserName', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This Email has already registered!')

    def validate_UserName(self, field):
        if User.query.filter_by(UserName=field.data).first():
            raise ValidationError('UserName is already in use!')


class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[DataRequired(), EqualTo('password2',
                                                                                 message='Passwords must be match')])
    password2 = PasswordField('Confirm your new password', validators=[DataRequired()])
    change_password = SubmitField('Change password')


class PasswordResetRequestFrom(Form):
    email = StringField('Enter your register email', validators=[DataRequired(), Email(), Length(1, 64)])
    submit = SubmitField('Send confirm email Link')


class PasswordResetForm(Form):
    email = StringField('Enter your email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Enter new password', validators=[DataRequired(),
                                                               EqualTo('password2', message='Passwords must be match')])
    password2 = PasswordField('Confirm your new password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')


class ChangeEmailForm(Form):
    email = StringField('Enter your new email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit = SubmitField('Update email address')

    def validate_email(self, filed):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('Email address is already exists.')
