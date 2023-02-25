from flask import Flask, render_template, redirect, request
import json


def users():
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    return render_template('users.html', users=users)


def removeUser(username):
    if username:
        with open('data/users.json', 'r') as f:
            users = json.load(f)
        users.pop(username)
        with open('data/users.json', 'w') as file:
            json.dump(users, file)
    return redirect('/users')


def editUser(username):
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    user_info = users[username]
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users[username]['email'] = email
        users[username]['password'] = password
        with open('data/users.json', 'w') as file:
            json.dump(users, file)
        return redirect('/')
    return render_template('edit_user.html', username=username, user_info=user_info)
