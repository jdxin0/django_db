# minidjango
* a simple way to use django orm in not django project
* multi databases support

```
from django.db import models
from minidjango import add_db

# django db configure
db_config = {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'NAME': 'test',
    'USER': 'test',
    'PASSWORD': 'test',
    'CONN_MAX_AGE': 0,
}

_app_lable = add_db(db_config)


class Test(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        app_label = _app_lable
        db_table = 'test'


if __name__ == '__main__':
    Test.create(id=1, name='test')
```
