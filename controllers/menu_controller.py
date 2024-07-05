from flask import render_template, request, redirect# type:ignore
from config import db
from models.menu import Menu

def index():
    menus = Menu.query.all()
    return render_template('/staff/menu.html', title="Menu Page", menus=menus)

def add_menu():
    return render_template('/create/create_menu.html', title="Add Menu")

def view_menu(id):
    menus = Menu.query.get(id)
    return render_template('/view/menu_profile.html', title="User Detail Page", menus=menus)

def newMenu():
    form = request.form
    img = form['img']
    menu_name = form['menu_name']
    price = form['price']
    description = form['description']

    menus = Menu(menu_name=menu_name, price=price, description=description, img=img)
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
