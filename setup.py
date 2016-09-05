from setuptools import setup


setup(
    name='django_db',
    version='0.0.6',
    url='https://github.com/jdxin0/django_db',
    description='A simple way to use django orm not in a classic django project',
    author='jdxin0',
    author_email='jdxin00@gmail.com',
    license='MIT',
    keywords='django orm db',
    packages=[
        'django_db',
    ],
    install_requires=[
        'django',
        'pymysql',
    ],
)
