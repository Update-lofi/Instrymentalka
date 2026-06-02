import re
from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired, NumberRange, ValidationError

def validate_phone(form, field):
    pattern = r'^((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}$'
    if not re.match(pattern, field.data):
        raise ValidationError('Неверный формат номера телефона.')

def validate_email(form, field):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    if not re.match(pattern, field.data):
        raise ValidationError('Неверный формат электронной почты.')

class PersonForm(Form):
    class Meta:
        csrf = False  # Отключаем CSRF защиту
    
    id = IntegerField('Идентификатор', validators=[DataRequired(message='Идентификатор обязателен для заполнения.')])
    name = StringField('Имя', validators=[DataRequired(message='Имя обязательно для заполнения.')])
    age = IntegerField('Возраст', validators=[
        DataRequired(message='Возраст обязателен для заполнения.'),
        NumberRange(min=1, max=200, message='Число должно быть между 1 и 200.')
    ])
    phone = StringField('Телефон', validators=[validate_phone])
    email = StringField('Электронная почта', validators=[validate_email])

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