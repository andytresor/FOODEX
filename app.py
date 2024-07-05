from flask import Flask
from flask_migrate import Migrate # type: ignore
from config import db

from routes.web_route import web
from routes.menu_route import menu
from routes.order_route import order
from routes.staff_route import staff
from routes.admin_route import admin
from routes.auth_route import auth

app = Flask(__name__)

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(web, url_prefix='/')
app.register_blueprint(menu, url_prefix='/menu')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(staff, url_prefix='/staff')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True, port=3000)