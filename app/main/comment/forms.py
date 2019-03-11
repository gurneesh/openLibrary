# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField(u"Your book review",
                            validators=[DataRequired(message=u"the content can not be blank"), Length(1, 1024, message=u"Book review length is limited to 1024 characters")])
    submit = SubmitField(u"release")
