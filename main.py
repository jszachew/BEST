# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, request, render_template


app = Flask(__name__, template_folder='template')

messages = []


@app.route('/messages')
def message():
    cookie_v = int(request.cookies.get('PHPSESSID'), 16)
    message_p = request.args.get("message")
    csrf = int(request.args.get("csrf"), 16)
    result = cookie_v ^ csrf

    messages.append(message_p)
    f = open("results.txt", "a")
    f.write(str(result))
    f.close()
    return render_template('chat.html', messages=messages)


@app.route("/")
def chat():
    return render_template('chat.html', messages=messages)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
