from flask import Blueprint # type:ignore

from controllers.commands_controller import index, commands, delete_command

command = Blueprint('command' , __name__)

command.route('/' , methods=['GET'] , strict_slashes=False)(index)
command.route('/command' , methods=['GET'] , strict_slashes=False)(commands)
command.route('/delete/<command_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_command)