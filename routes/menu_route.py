from flask import Blueprint # type:ignore

from controllers.menu_controller import index, add_menu, view_menu, newMenu, delete_menu, update_menu

menu = Blueprint('menu' , __name__)

menu.route('/' , methods=['GET'] , strict_slashes=False)(index)
menu.route('/add_menu' , methods=['GET'] , strict_slashes=False)(add_menu)
menu.route('/create_menu' , methods=['POST'] , strict_slashes=False)(newMenu)
menu.route('/view/<menu_id>' , methods=['GET'] , strict_slashes=False)(view_menu)
menu.route('/update/<menu_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update_menu)
menu.route('/delete/<menu_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_menu)
