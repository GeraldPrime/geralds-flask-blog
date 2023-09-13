from flask import session, redirect
from functools import wraps

def authenticate(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("ADMIN_LOGIN"):
            return redirect("/owner/")
        return fn(*args, **kwargs)
    return wrapper

def guest(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if session.get("ADMIN_LOGIN"):
            return redirect("/owner/dashboard")
        return fn(*args, **kwargs)
    return wrapper

# def check(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         # conn, cursor = db
#         query = "SELECT * FROM admin"
#         cursor.execute(query)
#         conn.commit()
#         admin = cursor.fetchall()
#         if admin:
#             # flash("Failed to register admin", "error")
#             return redirect("/owner/")
#     return wrapper    
