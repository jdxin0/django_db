from django_db import create_model, delete_model

from .models import Model1, Model2, Model3, clean_up
from .models2 import Model4


def test_create_model():
    create_model(Model1)
    Model1.objects.create(id=1, name='test')
    assert Model1.objects.get(id=1).name == 'test'
    delete_model(Model1)


def test_multi_db():
    list(map(create_model, [Model2, Model3, Model4]))
    Model2.objects.create(id=1, name='test')
    assert Model2.objects.get(id=1).name == 'test'
    Model3.objects.create(id=1, name='test')
    assert Model3.objects.get(id=1).name == 'test'
    Model4.objects.create(id=1, name='test')
    assert Model4.objects.get(id=1).name == 'test'
    list(map(delete_model, [Model2, Model3, Model4]))


if __name__ == '__main__':
    test_create_model()
    test_multi_db()
    clean_up()
