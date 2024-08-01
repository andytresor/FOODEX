from flask import render_template, request, redirect, session, flash# type:ignore
from config import db
from models.command import Commands
from models.order import Order

def index():
    commands = Commands.query.all()
    return render_template('/cook/display.html', title="Home Page", commands=commands)

def commands():
    return render_template('/cook/display.html')

def newCommand():   
    orders = Order.query.all()

    if not orders:
        print('No orders found for the user.')
        return redirect('/menu')
    
    total_price = 0
    total_qty = 0
    items = []
    for order in orders:
        qty = int(request.form.get(f'qty_{order.order_id}', 1))
        order_price = order.menu.price
        total_price += qty * order_price
        total_qty += qty
        items.append({'order_id': order.order_id, 'qty': qty})

    if total_qty > 0:
        command = Commands(
                total_qty = sum(int(request.form.get(f'qty_{order.order_id}', 1)) for order in orders),  # Sum of all quantities
                order_id=order.order_id,  # Use the first order's ID for the command
                items=items,
                total_price=total_price
            )
        db.session.add(command)
        db.session.commit()
        print('Command created successfully.')
    else:
        print('No quantities found in the form.')    

    return redirect('/menu')


def delete_command(command_id):
    if request.method == 'POST':
        if request.form['_method'] == 'DELETE':
            commands = Commands.query.get(command_id)
            db.session.delete(commands)
            db.session.commit()
            return redirect('/order')
    

# def update_Order(order_id):
#     orders = Order.query.filter_by(order_id = order_id).first()
#     if orders is None:
#         return redirect('/staff/staff')
#     if request.method == "GET":
#         return  render_template('/orders/modify_orders.html', title="Update Order Page", orders=orders)
#     elif request.method == "POST":
#         form = request.form
#         menu_name = form['menu_name']
#         price = form['price']
#         description = form['description']
#         client_name = form['client_name']
#         orders.client_name = client_name
#         orders.menu_name = menu_name
#         orders.email = price
#         orders.description = description
#         db.session.commit()
#         return redirect('/order/order')
#     return render_template('modify.html', title="Update Order Page", orders=orders)
