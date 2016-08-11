from setuptools import setup


setup(
    name='django_db',
    version='0.0.1',
    url='https://github.com/jdxin0/django_db',
    description='A simple way to use django orm not in a classic django project',
    author='jdxin0',
    author_email='jdxin00@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='django orm db',
    packages=[
        'django_db',
    ],
    install_requires=[
        'django',
        'pymysql',
    ],
)
