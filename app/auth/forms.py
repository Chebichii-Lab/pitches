from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from flask_wtf import FlaskForm
from ..models import User


class RegistrationForm(FlaskForm):
    """
    RegstrationForm class that passes in the required details for validation
    """

    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Your Username', validators=[Required()])
    password = PasswordField('  Password', validators=[Required(), EqualTo('password',message='passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')


    #custom validators
    def validate_email(self, data_field):
        """
        Functions takes in the data field and checks our database to confirm user Validation
        """
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Sorry, the account already exists with that email')


    def validate_username(self, data_field):
        """
        Function checks if the username is unique and raises ValidationError
        """
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Sorry, this user name is already taken. Try another one')


#login class  takes three inputs from the user
class LoginForm(FlaskForm):
    email = StringField('Your email address', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')