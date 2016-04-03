from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, DataRequired, Email, ValidationError
from ..models import Role, User
from flask.ext.login import current_user
from flask.ext.pagedown.fields import PageDownField


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(Form):
    name = StringField('Rela name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
    UserName = StringField('UserName', validators=[DataRequired(), Length(1, 64)])
    confirmed = BooleanField('confirmed')
    role = SelectField('Role', choices=[(1, 'Administrator'), (2, 'Moderator'), (3, 'User')], coerce=int)
#    role = SelectField('Role')
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    '''
    def __int__(self, user, *args, **kwargs):
        print '11111111111111'
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.RoleName).all()]
        self.user = user
    '''
    def validate_email(self, field):
        if field.data != current_user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already register.')

    def validate_UserName(self, field):
        if field.data != current_user.UserName and User.query.filter_by(UserName=field.data).first():
            raise ValidationError('UserName is already in use.')


class PostForm(Form):
    body = PageDownField("what is on your mind?", validators=[DataRequired()])
    submit = SubmitField('submit')


class CommentForm(Form):
    body = PageDownField('Comment', validators=[DataRequired()])
    submit = SubmitField('submit')

