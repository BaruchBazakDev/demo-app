from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')


class Employee(FlaskForm):
    f_name = StringField('First name', validators=[InputRequired(),
                                                   Length(min=2, max=24)])

    l_name = StringField('Last name', validators=[InputRequired(),
                                                  Length(min=2, max=24)])

    city = StringField('City', validators=[InputRequired(),
                                           Length(min=2, max=24)])

    address = StringField('Address', validators=[InputRequired(),
                                                 Length(min=2, max=24)])

    phone_number = StringField('phone_number', validators=[InputRequired(),
                                                           Length(min=7, max=12)])
