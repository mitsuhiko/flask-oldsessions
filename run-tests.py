import sys
from flask import Flask
import flask_oldsessions
from flask.testsuite import main


def _run_test(name):
    sys.argv[:] = sys.argv[:1]
    cls = getattr(flask_oldsessions, name)
    Flask.session_interface = cls()
    main()


_run_test(sys.argv[1])
