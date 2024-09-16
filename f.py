from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,FileField,SubmitField,BooleanField,validators
from config import *
from flask_ckeditor import CKEditorField


class login_form(FlaskForm):
    username = StringField('username',validators=[
        validators.DataRequired()
    ])
    password = PasswordField('passwsord',validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('submit')

class register_form(FlaskForm):
    email = StringField('email',validators=[
        validators.DataRequired(),
        validators.Email()
    ])
    username = StringField('username',validators=[
        validators.Length(min=5,max=20)
    ])
    password = PasswordField('passwsord',validators=[
        validators.DataRequired(),
        validators.Length(min=8,max=20)
    ])
    confirm = PasswordField('passwsord',validators=[
        validators.DataRequired(),
        validators.EqualTo('password')
    ])
    submit = SubmitField('submit')

class post_form(FlaskForm):
    title = StringField('title',validators=[
        validators.DataRequired(),
        validators.Length(min=5,max=20)
    ])
    body = CKEditorField('body',validators=[
        validators.DataRequired(),
        validators.Length(min=5,max=2000)
    ])
    img = FileField('img',validators=[
        validators.Required()
    ])
    submit = SubmitField('submit')


class post_edit_form(FlaskForm):
    title = StringField('title',validators=[
        validators.DataRequired(),
        validators.Length(min=5,max=20)
    ])
    body = TextAreaField('body',validators=[
        validators.DataRequired(),
        validators.Length(min=5,max=2000)
    ])
    # img = FileField('img',validators=[
    #     validators.Required()
    # ])
    dont_want_image = BooleanField('image')
    submit = SubmitField('submit')

class prof_edit_form(FlaskForm):
    username = StringField('username',validators=[
        validators.Length(min=5,max=20)
    ])

class comment_form(FlaskForm):
    body = TextAreaField('body',validators=[
        validators.DataRequired(),
        validators.Length(min=5,max=2000)
    ])
    submit = SubmitField('submit')
