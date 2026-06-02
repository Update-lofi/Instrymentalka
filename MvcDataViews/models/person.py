import re
from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired, NumberRange, ValidationError

def validate_phone(form, field):
    pattern = r'^((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}$'
    if not re.match(pattern, field.data):
        raise ValidationError('Invalid phone number.')

def validate_email(form, field):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    if not re.match(pattern, field.data):
        raise ValidationError('Invalid email address.')

class PersonForm(Form):
    id = IntegerField('ID', validators=[DataRequired(message='The ID is required.')])
    name = StringField('Name', validators=[DataRequired(message='The name is required.')])
    age = IntegerField('Age', validators=[
        DataRequired(),
        NumberRange(min=1, max=200, message='A number between 1 and 200.')
    ])
    phone = StringField('Phone', validators=[validate_phone])
    email = StringField('Email', validators=[validate_email])

class Person:
    def __init__(self, id, name, age, phone, email):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'email': self.email
        }