from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, ValidationError
from constants import *

class LoginForm(FlaskForm):
    answer = StringField("userId")

    def __init__(self, *args, **kwargs):
        #kwargs['csrf_enabled'] = False
        super(LoginForm, self).__init__(*args, **kwargs)
    
    def validate_answer(self, answer):
        if len(answer.data) > 100:
            raise ValidationError(ERR3)
        if answer.data == "":
            raise ValidationError(ERR5)
        if not answer.data.encode("utf-8").isalnum():
            raise ValidationError(ERR4)
            
