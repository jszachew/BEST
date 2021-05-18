# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from typing import Callable


class MySQLAlchemy(SQLAlchemy):  # Or you can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable


app = Flask(__name__, template_folder='template')

messages = []


@app.route('/messages')
def message():
    cookie_v = int(request.cookies.get('PHPSESSID'), 16)
    message_p = request.args.get("message")
    csrf = int(request.args.get("csrf"), 16)
    result = cookie_v ^ csrf

    messages.append(message_p)
    print(result)
    return str(result)


@app.route("/")
def chat():
    return render_template('chat.html', messages=messages)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
