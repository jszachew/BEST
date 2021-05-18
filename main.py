# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, request

app = Flask(__name__)


@app.route('/message')
def best():
    cookie_v = int(request.cookies.get('PHPSESSID'), 16)
    csrf = int(request.args.get("csrf"), 16)
    result = cookie_v ^ csrf
    print(result)
    return str(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
