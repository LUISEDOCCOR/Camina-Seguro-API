from functools import wraps
from flask import session, redirect, url_for

def requires_login(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if ("username" not in session and "id" not in session):
            return redirect(url_for("localauth.login"))
        else:
            return f(*args, **kwargs)
    return decorator