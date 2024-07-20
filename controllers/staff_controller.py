from flask import render_template, request, redirect, session
from config import db
from models.staff import Staff
from werkzeug.utils import secure_filename

def index():
    staffs = Staff.query.all()
    return render_template('/staff/menu.html', title="Home Page", staffs=staffs)

def members():
    staffs = Staff.query.all()
    return render_template('members.html', title="Home Page", staffs=staffs)

def membersTwo():
    staffs = Staff.query.all()
    return render_template('dashboard.html', title="Home Page", staffs=staffs)

def add_staff():
    return render_template('/create/create_staff.html', title="Add Staff")


# def cook_index():
#     return render_template('/cook/display.html', title="Add Staff")

def view_staff(id):
    staffs = Staff.query.get(id)
    return render_template('/view/staff_profile.html', title="User Detail Page", staffs=staffs)

def newStaff():
    form = request.form
    img = request.files['img']
    img.save(img.filename)
    name = form['name']
    email = form['email']
    password = form['password']
    salary = form['salary']
    role = form['role']

    if not img:
        return 'no pic upload'
     
    filename = secure_filename(img.filename)
    mimetype = img.mimetype

    staff = Staff(name=name, password=password, email=email, salary=salary, role=role, img=img.filename, img_name=filename, mimetype=mimetype)
    db.session.add(staff)
    db.session.commit()

    return redirect('/admin')

def delete_staff(staff_id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            users = Staff.query.get(staff_id)
            db.session.delete(users)
            db.session.commit()
            return redirect('/admin')
    

def update_staff(staff_id):
    staffs = Staff.query.filter_by(staff_id = staff_id).first()
    if staffs is None:
        return redirect('/admin')
    if request.method == "GET":
        return  render_template('/update/modify_staff.html', title="Update Page", staffs=staffs)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        salary = form['salary']
        role = form['role']
        staffs.email = email
        staffs.salary = salary
        staffs.role = role
        staffs.name = name
        db.session.commit()
        return redirect('/admin')
    return render_template('/update/modify_staff.html', title="Update Page", staffs=staffs)

def logout():
    if 'staff_id' in  session:
        session.pop('staff_id', None)
    if 'staff_name' in  session:
        session.pop('staff_name', None)
    if 'role' in  session:
        session.pop('role', None)
    return redirect('/auth/staff_type')
