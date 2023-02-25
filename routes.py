import json
from flask import Flask, render_template, request, session, redirect
from calculator import calculator
from login import login
from register import register
from users import users as usersRoute, removeUser, editUser

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

with open('data/users.json', 'r') as file:
    users = json.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator_route():
    if request.method == 'POST':
        return calculator()
    else:
        return render_template('calculator.html')


@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        return login(users)
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'POST':
        return register(users)
    else:
        return render_template('register.html')


@app.route('/users')
def users_route():
    return usersRoute()


@app.route('/clear_session', methods=['POST'])
def clear_session():
    session.clear()
    return redirect('/')


@app.route('/edit_user/<username>', methods=['GET', 'POST'])
def edit_user(username):
    return editUser(username)


@app.route('/remove_user/<username>', methods=['POST'])
def remove_user(username):
    return removeUser(username)


if __name__ == '__main__':
    app.run(debug=True)
