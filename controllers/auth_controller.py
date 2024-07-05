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
     if user.User_type != user_type:
         return redirect('auth/login', message="invalid Credential!!")
     if user_type == "admin".toLowerCase():
         return redirect('/admin')
     if user_type == "cook".toLowerCase():
         return redirect('/staff/display')
     if user_type == "servant".toLowerCase():
         return redirect('/staff')
     session['auth'] = {
        "id": user.user_id,
        "username": user.user_name
    }
     return redirect('/')

def staff_type():
    return render_template('/auth/user_type.html')

def login_staff():
     form = request.form
     user_type = form['user_type']
     
     user = Staff.query.filter_by(user_type=user_type).first()
     if user.user_type != user_type:
         return redirect('/auth/login', message="invalid Credential!!")
     if user_type == "admin".toLowerCase():
         return redirect('/admin')
     if user_type == "cook".toLowerCase():
         return redirect('/cook/display.html')
     if user_type == "servant".toLowerCase():
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
     password = form['password']
     cpassword = form['cpassword']

     if password != cpassword:
         return redirect('/auth/register', message="Invalid Password")
     
     user = Auth.query.filter_by(email=email).first()
     if user:
         return redirect('/auth/register', message="User with this email aready exists!!")
     
     user = Auth(email=email, user_name=user_name, password=generate_password_hash(password))
     db.session.add(user)
     db.session.commit()
     return redirect('/auth/login')
     
     

#logout

def logout():
    if 'auth' in  session:
        session.pop('auth', None)
    return redirect('/auth/login')


