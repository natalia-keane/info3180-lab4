from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    upload=FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
