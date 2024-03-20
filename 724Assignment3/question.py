from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class DataCollection(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    student_number = StringField('Student P Number', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    grades = StringField('Grades Obtained', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    ], validators=[DataRequired()])
    favorite_subject = SelectField('Favorite Subject', choices=[
        ('FC-723 Programming Theory'),
        ('FC-724 Programming Practical Applications'),
        ('FC-701 Extended Project'),
        ('FC-703 Intermediate Mathematics')
    ], validators=[DataRequired()])
    suggestions = TextAreaField('Suggestions for Improvement', validators=[DataRequired()])
    recommendations = TextAreaField('Recommendations for Future Students')