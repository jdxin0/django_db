from django_db import add_db
from .models import Test

db_config3 = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test3.sqlite3'
}
_app_label3 = add_db(db_config3)


class Model4(Test):
    class Meta:
        app_label = _app_label3
        db_table = 'model4'