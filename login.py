from flask import redirect, render_template, request, session


def login(users):
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]['password'] == password:
        session['username'] = username
        return redirect('/')
    else:
        error_message = 'Invalid username or password'
        return render_template('login.html', error_message=error_message)