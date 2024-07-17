from flask import render_template, request, redirect, session# type:ignore
from config import db
from models.auth import Auth

def index():
    admins = Auth.query.all()
    return render_template('dashboard.html', title="Dashboard Page", admins=admins)

def profile():
    getsession = session.get('auth')
    userName = getsession.username
    if userName is not None:
        print(userName)
    else:
        print('user not found')

# def add_admin():
#     return render_template('dashboard.html', title="Add Admin")

def view_admin(admin_id):
    admin = Auth.query.get(admin_id)
    return render_template('/view/admin_profile.html', title="Admin Detail Page", admin=admin)

# def newAdmin():
#     form = request.form
#     name = form['name']
#     email = form['email']

#     admin= Admin(name=name, email=email)
#     db.session.add(admin)
#     db.session.commit()

#     return redirect('/admin')

def update_admin(admin_id):
    admin = Auth.query.filter_by(admin_id = admin_id).first()
    if admin is None:
        return redirect('/admin')
    if request.method == "GET":
        return  render_template('/update/modify_admin.html', title="Update Page", admin=admin)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        admin.email = email
        admin.name = name
        db.session.commit()
        return redirect('/admin')
    return render_template('/update/modify_admin.html', title="Update Page", admin=admin)
