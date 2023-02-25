from flask import redirect, request
import json


def register(users):
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return 'Passwords do not match'

    if username in users:
        return 'Username already exists'

    users[username] = {'email': email, 'password': password}

    with open('data/users.json', 'w') as file:
        json.dump(users, file)

    return redirect('/login')
