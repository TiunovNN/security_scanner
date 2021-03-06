from flask_login import current_user
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, FormField, HiddenField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from web import models
from web.validators import UniqueRequired, HostnameRequired


def get_profiles():
    return current_user.scan_profiles


class TaskSettingForm(FlaskForm):
    hostname = StringField(_l('Hostname'),
                           validators=[HostnameRequired(allow_ip=True)])
    profile = QuerySelectField(
        _l('Profile'),
        get_label='name',
        query_factory=get_profiles
    )

    def __init__(self, *args, **kwargs):
        super().__init__(csrf_enabled=False, *args, **kwargs)


class TaskForm(FlaskForm):
    id = HiddenField(_l('Id'))
    name = StringField(
        _l('Name'),
        validators=[
            DataRequired(),
            UniqueRequired(models.Task, 'name')
        ])
    settings = FieldList(FormField(TaskSettingForm))
    submit = SubmitField(_l('Save'))

    def populate(self, task):
        self.id.data = task.id
        self.name.data = task.name
        for setting in task.settings:
            setting_form = TaskSettingForm()
            setting_form.hostname = setting.hostname
            setting_form.profile = setting.profile
            self.settings.append_entry(setting_form)
