from flask import render_template, request, redirect# type:ignore
from config import db
from models.admin import Admin

def index():
    admin = Admin.query.all()
    return render_template('dashboard.html', title="Dashboard Page", admin=admin)

# def add_admin():
#     return render_template('dashboard.html', title="Add Admin")

def view_admin(admin_id):
    admin = Admin.query.get(admin_id)
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
    admin = Admin.query.filter_by(admin_id = admin_id).first()
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
