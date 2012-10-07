from setuptools import setup


setup(
    name='Flask-OldSessions',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='0.10',
    url='http://github.com/mitsuhiko/flask-oldsessions',
    py_modules=['flask_oldsessions'],
    description='Provides a session class that works like the one in Flask before 0.10.',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
