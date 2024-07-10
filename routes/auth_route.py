from flask import Blueprint

from controllers.auth_controller import login, register,staff_type, login_user,login_staff, register_user, logout

auth = Blueprint('auth', __name__)

auth.route('/login', methods=['GET'], strict_slashes=False)(login),
auth.route('/staff_type', methods=['GET'], strict_slashes=False)(staff_type),
auth.route('/register', methods=['GET'], strict_slashes=False)(register)
auth.route('/login_user', methods=['POST'], strict_slashes=False)(login_user),
auth.route('/login_staff', methods=['POST'], strict_slashes=False)(login_staff),
auth.route('/register_user/<user_id>', methods=['GET','POST'], strict_slashes=False)(register_user),
auth.route('/logout', methods=['POST', 'DELETE'], strict_slashes=False)(logout)