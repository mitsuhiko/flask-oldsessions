Flask-OldSessions
=================

.. module:: flask_oldsessions

Flask-OldSessions is an extension to `Flask`_ that reimplements the old
pickle based session interface from Flask 0.9 and earlier for backwards
compatibility reasons.

Installation
------------

Install the extension with one of the following commands::

    $ pip install Flask-OldSessions

Alternatively, use `easy_install`::

    $ easy_install Flask-OldSessions

.. _Flask: http://flask.pocoo.org/

Usage
-----

To use this session interface with Flask you can use it to replace the
one that comes by default.  Just import the
:class:`OldSecureCookieSessionInterface` and attach it to the
application::

    from flask import Flask
    from flask_oldsessions import OldSecureCookieSessionInterface

    app = Flask(__name__)
    app.session_interface = OldSecureCookieSessionInterface()


API Reference
-------------

.. autoclass:: OldSecureCookieSessionInterface
   :members:

.. autoclass:: UpgradingSessionInterface
   :members:
