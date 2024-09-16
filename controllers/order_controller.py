from flask import render_template, request, redirect, session# type:ignore
from config import db
from models.order import Order


def index():
    orders = Order.query.all()
    print(orders)
    return render_template('/staff/cart.html', title="Home Page", orders=orders)

def view_order():
    user_id = session.get('staff_id')  # Get user ID from session
    orders = Order.query.filter_by(user_id=user_id).all()
    cart_count = db.session.query(db.func.sum(Order.order_id)).scalar() or 0
    print(cart_count)
    return render_template('/staff/cart.html', orders=orders, cart_count=cart_count)


def orders():
    return render_template('/staff/cart.html', title="Add Order")


def newOrder():
    user_id = session.get('user_id')
    menu_id = Order.query.filter_by(user_id=user_id).all()

    orders = Order(user_id=user_id, menu_id=menu_id)
    db.session.add(orders)
    db.session.commit()

    return redirect('/order/order')


def delete_order(order_id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            orders = Order.query.get(order_id)
            db.session.delete(orders)
            db.session.commit()
            return redirect('/order')
    
