import functools
from web_server.model.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/allusers', methods=('GET', 'POST'))
def getAll():
    db = get_db()
       
    users = db.execute(
        'SELECT * FROM user')
    ## DO not work need to convert sqlite object to json and return
    return str(users)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """
        EndPoint for register an User:
        - username
        password
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("FOR REGISTRATION: username:"+username+", pwd:"+password)
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    """
     EndPoint for authenticate an User:
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("Data received on /auth/login username:"+username+", pwd:"+password)
        
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')