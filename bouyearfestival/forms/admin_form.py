from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, ValidationError
from constants import *

class AdminForm(FlaskForm):
    answer3 = StringField("processId")

    def __init__(self, *args, **kwargs):
        #kwargs['csrf_enabled'] = False
        super(AdminForm, self).__init__(*args, **kwargs)
    
    def validate_answer3(self, answer3):
        if len(answer3.data) > 100:
            raise ValidationError(ERR3)
        if answer3.data == "":
            raise ValidationError(ERR5)
        if not answer3.data.encode("utf-8").isalnum():
            raise ValidationError(ERR4)
            
