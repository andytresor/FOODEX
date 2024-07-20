from flask import render_template, redirect, request, session, url_for # type: ignore
from models.auth import Auth
from models.staff import Staff
from werkzeug.security import generate_password_hash, check_password_hash
from config import db

def login():
    return render_template('/auth/login.html')

def profile():
    user_id = session.get('user_id')
    print(user_id)
    return render_template('/update/modify_staff.html', user_id=user_id)

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
     
     session['auth'] = {
        "id": user.user_id,
        "username": user.user_name,
        "user_type": user.user_type
    }
     if user_type == "cook":
         return redirect('/staff/display')
     
     if user_type == "servant":
         return redirect('/staff')
     return redirect('/')

def staff_type():
    return render_template('/auth/user_type.html')

def login_staff():
    form = request.form.get
    email = form('email')
    role = form('role')
    password = form('password')

    staff = Staff.query.filter_by(email=email).first()
    if not staff:
        return redirect(url_for('auth.login', message="Account doesn't Exists!"))

    if staff.password != password:
        return redirect(url_for('auth.login', message="Please Check Password!"))

    if staff.role != role:
        return redirect(url_for('auth.login', message="Invalid UserType!"))
    
    # Store user information in the session
    session['staff_id'] = staff.staff_id
    session['staff_name']= staff.name
    session['role']= staff.role
    
    
    print(f"Session set: staff_id={session['staff_id']}")
    
    if role == "cook":
         return redirect(url_for('staff.cook_page', message="Welcome"))
    
    if role == "servant":
         return redirect(url_for('menu.index', message="Welcome"))
    
    return redirect(url_for('index'))   
     

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
     
     user = Auth(email=email, user_name=user_name, password=generate_password_hash(password), user_type='admin')
     db.session.add(user)
     db.session.commit()
     return redirect('/auth/login')
     
     

#logout

def logout():
    if 'auth' in  session:
        session.pop('auth', None)
    return redirect('/auth/staff_type')


