# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired, Optional

class EmployeeForm(Form):
    first_name = StringField(u'Nombre', validators=[DataRequired()])
    last_name = StringField(u'Apellido', validators=[DataRequired()])
    birth_date = DateField(u'Fecha Nacimiento', validators=[DataRequired()])
    cuil = StringField(u'C.U.I.L.', validators=[DataRequired()])
    hire_date = DateField(u'Fecha Contratación', validators=[DataRequired()])
    user_code = IntegerField(u'Código Reloj', validators=[DataRequired()])    
    file_no = IntegerField(u'Legajo', validators=[Optional()])
