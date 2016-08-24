import os
from django.db import models
from django_db import add_db


class Test(models.Model):
    name = models.CharField(max_length=5)

    class Meta:
        abstract = True
        app_label = 'test'


db_config = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test.sqlite3'
}
_app_label = add_db(db_config)


class Model1(Test):
    class Meta:
        app_label = _app_label
        db_table = 'model1'


class Model2(Test):
    class Meta:
        app_label = _app_label
        db_table = 'model2'


db_config2 = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test2.sqlite3'
}
_app_label2 = add_db(db_config2)


class Model3(Test):
    class Meta:
        app_label = _app_label2
        db_table = 'model3'


def clean_up():
    for i in [i for i in os.listdir('.') if i.endswith('.sqlite3')]:
        os.remove(i)
        print('remove database {}'.format(i))
