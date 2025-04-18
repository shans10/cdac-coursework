from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=150)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=150)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # Custom validator to check if username is already taken
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Username is already taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Login')


class GrievanceForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=5, max=200)])
    description = TextAreaField('Description',
                                validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Grievance')


class UpdateStatusForm(FlaskForm):
    status = SelectField('Status',
                         choices=[('Pending', 'Pending'),
                                  ('In Progress', 'In Progress'),
                                  ('Resolved', 'Resolved')],
                         validators=[DataRequired()])
    submit = SubmitField('Update Status')
