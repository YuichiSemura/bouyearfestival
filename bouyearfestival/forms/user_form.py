from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, ValidationError
from constants import *

class UserForm(FlaskForm):
    answer2 = StringField("processId")

    def __init__(self, *args, **kwargs):
        #kwargs['csrf_enabled'] = False
        super(UserForm, self).__init__(*args, **kwargs)
    
    def validate_answer2(self, answer2):
        if len(answer2.data) > 100:
            raise ValidationError(ERR3)
        if answer2.data == "":
            raise ValidationError(ERR5)
        if not answer2.data.encode("utf-8").isalnum():
            raise ValidationError(ERR4)
            
