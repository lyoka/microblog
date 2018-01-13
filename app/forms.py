from flask_wtf import FlaskForm
from wtforms.fields import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(FlaskForm):
  openid = TextField('openid', validators = [Required()])
  remember_me = BooleanField('remember_me', default = False)
