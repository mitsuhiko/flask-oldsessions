# -*- coding: utf-8 -*-
"""
    flask_oldsessions
    ~~~~~~~~~~~~~~~~~

    Implements cookie based sessions based on Werkzeug's secure cookie
    system.

    :copyright: (c) 2011 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from werkzeug.contrib.securecookie import SecureCookie

from flask.sessions import SessionMixin, SessionInterface, \
     SecureCookieSessionInterface


class OldSecureCookieSession(SecureCookie, SessionMixin):
    """Expands the session with support for switching between permanent
    and non-permanent sessions.
    """


class OldSecureCookieSessionInterface(SessionInterface):
    """The cookie session interface that uses the Werkzeug securecookie
    as client side session backend.
    """
    session_class = OldSecureCookieSession

    def open_session(self, app, request):
        key = app.secret_key
        if key is not None:
            return self.session_class.load_cookie(request,
                                                  app.session_cookie_name,
                                                  secret_key=key)

    def save_session(self, app, session, response):
        expires = self.get_expiration_time(app, session)
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        if session.modified and not session:
            response.delete_cookie(app.session_cookie_name, path=path,
                                   domain=domain)
        else:
            session.save_cookie(response, app.session_cookie_name, path=path,
                                expires=expires, httponly=httponly,
                                secure=secure, domain=domain)


class UpgradingSessionInterface(SessionInterface):
    """A session interface that upgrades from one session system to
    another one.

    :param old_interface: the old session interface to use.
                          :class:`OldSecureCookieSessionInterface`.
    :param new_interface: the new session interface to use.
                          :class:`flask.sessions.SecureCookieSessionInterface`
    """

    def __init__(self, old_interface=None, new_interface=None):
        if old_interface is None:
            old_interface = OldSecureCookieSessionInterface()
        if new_interface is None:
            new_interface = SecureCookieSessionInterface()
        self.old_interface = old_interface
        self.new_interface = new_interface

    @property
    def null_session_class(self):
        return self.new_interface.null_session_class

    @property
    def pickle_based(self):
        return self.new_interface.pickle_based

    @property
    def session_class(self):
        return self.new_interface.session_class

    def is_null_session(self, obj):
        return self.new_interface.is_null_session(obj) or \
               self.old_interface.is_null_session(obj)

    def open_session(self, app, request):
        rv = self.new_interface.open_session(app, request)
        if rv is None:
            rv = self.old_interface.open_session(app, request)
            # Upgrade the session class (this might very well break :()
            if rv is not None and not self.is_null_session(rv) and \
               not isinstance(rv, self.new_interface.session_class):
                rv = self.new_interface.session_class(rv)
        return rv

    def save_session(self, app, session, response):
        return self.new_interface.save_session(app, session, response)
