from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField,SelectField,FloatField,validators
from wtforms.validators import DataRequired

class Ale_form(FlaskForm):
      username = StringField('Name', validators=[DataRequired()])
      weight=FloatField("How much do you weight(kg)?",validators=[DataRequired()])
      height=FloatField("How tall are you(cm)?",validators=[DataRequired()])
      diabetes=SelectField("Do you have diabetes?",
                           choices=[('0.5', 'Yes'), ('0.01', 'No')],
                           validators=[DataRequired()])
      smoke=SelectField("How many cigarettes a day do you smoke?(if you do not smoke choose <5)",
                           choices=[('1', 'less than 5'), ('2', 'between 5 and 9'),('3','between 10 and 20'),
                                                           ('4','between 20 and 30'),('5','between 30 and 39'),
                                                           ('6','more than 40')],
                           validators=[DataRequired()])
      exercise=SelectField("Do you do exercise regularly?",
                           choices=[('0.6', 'No'), ('0.1', 'Twice a week'),('0.01', 'Every day')],
                           validators=[DataRequired()])
      hsdiploma=SelectField("Do you have a High School diploma?",
                           choices=[('0.01', 'Yes'), ('0.5', 'No')],
                           validators=[DataRequired()])
      poverty=SelectField("How much money do you earn a year?",
                           choices=[('0.5', 'Less than 25k $'), ('0.01', 'More than 25k $')],
                           validators=[DataRequired()])
      
      submit = SubmitField('Submit')


