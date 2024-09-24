import os
from flask import app, jsonify, render_template, request, Response, redirect, session# type:ignore
from config import db
from models.menu import Menu
from models.order import Order
from werkzeug.utils import secure_filename

def index():
    menus = Menu.query.all()
    return render_template('/staff/menu.html', title="Menu Page", menus=menus)

# def cook():
#     orders = Order.query.all()
#     return render_template('/cook/display.html', title="Menu Page", orders=orders)
    

def add_menu():
    return render_template('/create/create_menu.html', title="Add Menu")


def view_menu(id):
    menus = Menu.query.get(id)
    return render_template('/view/menu_profile.html', title="User Detail Page", menus=menus)

def add_to_cart(menu_id):
    user_id = session.get('staff_id')
    if user_id is None:
        return jsonify(message='No user'), 401

    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify(message='Product Not Added'), 404

    # Check if the product is already in the cart
    existing_order = Order.query.filter_by(user_id=user_id, menu_id=menu_id).first()
    if existing_order:
        existing_order.quantity += 1
    else:
        new_order = Order(menu_id=menu_id, user_id=user_id, quantity=1)
        db.session.add(new_order)

    db.session.commit()
    return jsonify(message="Product Successfully Added")

def newMenu():
    form = request.form
    file = request.files['file']
    menu_name = form['menu_name']
    price = form['price']
    description = form['description']

    if not file:
        return ({"error: No Picture Uploaded"}, 400) 
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['upload_folder'], filename))
    mimetype = file.mimetype

    menus = Menu(menu_name=menu_name, price=price, description=description, img=file, filename=filename, mimetype=mimetype)
    db.session.add(menus)
    db.session.commit()

    return redirect('/menu')

def delete_menu(menu_id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            menus = Menu.query.get(menu_id)
            db.session.delete(menus)
            db.session.commit()
            return redirect('/menu')
    

def update_menu(menu_id):
    menus = Menu.query.filter_by(menu_id = menu_id).first()
    if menus is None:
        return redirect('/menu')
    if request.method == "GET":
        return  render_template('/update/modify_menu.html', title="Update Page", menus=menus)
    elif request.method == "POST":
        form = request.form
        img = form['img']
        menu_name = form['menu_name']
        price = form['price']
        description = form['description']
        menus.img = img
        menus.name = menu_name
        menus.email = price
        menus.phone = description
        db.session.commit()
        return redirect('/menu')
    return render_template('/update/modify.html', title="Update Menu Page", menus=menus)
