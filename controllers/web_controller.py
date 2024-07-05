from flask import render_template, session, redirect # type: ignore

def index():
    return render_template('index.html')

def account():
    if 'auth' in session:
        return render_template('menu.html')
    redirect('/login', message='Please login to your account')
