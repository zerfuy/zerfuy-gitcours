import functools
from web_server.model.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/add', methods=('GET', 'POST'))
def add():
    """
        EndPoint for register an User:
        - username
        password
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("username:"+str(username))
        print("password:"+str(password))
        db = get_db()
        error = None

        if not username:
            print('Username is required.')
            error = 'Username is required.'
        elif not password:
            print('Password is required.')
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            print ('User {} is already registered.'.format(username))
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, password)
            )

            db.commit()
            print("User:"+str(username)+" inserted into db")
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')