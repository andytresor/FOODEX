from flask import render_template, redirect, request, session # type: ignore
from models.auth import Auth
from models.staff import Staff
from werkzeug.security import generate_password_hash, check_password_hash
from config import db

def login():
    return render_template('/auth/login.html')

def login_user():
     form = request.form
     email = form['email']
     password = form['password']
     user_type = form['user_type']
     
     user = Auth.query.filter_by(email=email).first()
     if not user or not check_password_hash(user.password, password):
         return redirect('auth/login', message="invalid Credential!!")
     if user.user_type != user_type:
         return redirect('auth/login', message="invalid Credential!!")
     if user_type == "admin":
         return redirect('/admin')
     staff = Staff.query.filter_by(email=email).first()
     if not staff:
         return redirect('/auth/login')
     if staff.role != user_type:
         return redirect('/auth/register', message="invalid Credential!!")
     if user_type == "cook":
         return redirect('/staff/display')
     if user_type == "servant":
         return redirect('/staff')
     session['auth'] = {
        "id": user.user_id,
        "username": user.user_name,
        "user_type": user.user_type
    }
     return redirect('/')

def staff_type():
    return render_template('/auth/user_type.html')

def login_staff():
     form = request.form
     email = form['email']
     role = form['role']
     
     user = Staff.query.filter_by(email=email).first()
     if not user:
         return redirect('auth/login', message="invalid Credential!!")
     if user.role != role:
         return redirect('/auth/login', message="invalid Credential!!")
     if role == "cook":
         return redirect('/staff/display')
     if role == "servant":
         return redirect('/staff')
     session['auth'] = {
        "id": user.staff_id,
        "username": user.name
    }
     return redirect('/')     
     

#Register

def register():
    return render_template('/auth/register.html')

def register_user():
     form = request.form
     user_name = form['user_name']
     email = form['email']
     user_type = 'admin'
     password = form['password']
     cpassword = form['cpassword']

     if password != cpassword:
         return redirect('/auth/register', message="Invalid Password")
     
     user = Auth.query.filter_by(email=email).first()
     if user:
         return redirect('/auth/register', message="User with this email aready exists!!")
     
     user = Auth(email=email, user_name=user_name, password=generate_password_hash(password), user_type=user_type)
     db.session.add(user)
     db.session.commit()
     return redirect('/auth/login')
     
     

#logout

def logout():
    if 'auth' in  session:
        session.pop('auth', None)
    return redirect('/auth/staff_type')


