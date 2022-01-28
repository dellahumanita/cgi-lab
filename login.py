#!/usr/bin/python3
import cgi
import cgitb 
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret 
import os 
from http.cookies import SimpleCookie

field = cgi.FieldStorage()
username = field.getfirst("username")
password = field.getfirst("password")

# check if the cookie already exists 
# if the login info is already provided to the cgi form 
form_ok = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None 
cookie_password = None

if cookie.get("username"):
    cookie_username = cookie["username"].value
if cookie.get("password"):
    cookie_password = cookie["password"].value

# check if the cookie's username/password matches the secret username/password
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# if the cookie is ok, then set the username and password 
if cookie_ok:
    username = cookie_username
    password = cookie_password

# if there were no cookies, set the cookie iff the login info is correct 
print('Content-Type: text/html')
if form_ok:
    print(f'Set-Cookie: username={username}')
    print(f'Set-Cookie: password={password}')

print()

# load relevant html pages  
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
