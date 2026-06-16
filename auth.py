from db import register_user, login_user

def register(u, p):
    register_user(u, p)

def login(u, p):
    return login_user(u, p)