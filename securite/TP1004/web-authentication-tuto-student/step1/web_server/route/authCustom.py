#!flask/bin/python
import functools
import base64
import binascii
from web_server.model.db import get_db
import re
import hashlib
import random
import time
import uuid
import json
from web_server.tools.CipherTools import checkTokenSHA256,computeHashDIgest,generate_server_key,generate_VI,generateTokenSHA256

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,make_response
)

bp = Blueprint('authcustom', __name__, url_prefix='/authcustom')


def checkCredential(username, password):
    db = get_db()
    error = None
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    if user is None:
        error = 'Incorrect username:'+username
        print(error)
        return False
    elif not user['password']==password:

        error = 'Incorrect password:'+password
        print(error)
        return False
    return True

def _getUserPwd(username):
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    if user is None:
        return None
    return user['password']



@bp.route('/authbasic', methods=('GET', 'POST'))
def authBasic():
    """
        EndPoint for register an User:
        HTTP header authorization field contains : TODO
    """
    print("--------------- Basic Auth triggered --------------------")
    # only post is authorized
    if request.method == 'POST':
        # get the authorization field
        authorization_field_value=request.headers['authorization']
        print("[Authorization header field]:"+authorization_field_value)
        #############
        #
        # TODO
        #
        #############
        ## This return if success
        #return render_template('auth/successAuth.html')

    ## This return if failure occured
    return render_template('auth/login.html')

@bp.route('/authdigest', methods=('GET', 'POST'))
def authDigest():
    """
        EndPoint for register Digest Registration User:
        HTTP header authorization field contains : TODO
        This end point assumes that realm and nonce (add other options) has been already transmitted
        regex could be checked here https://pythex.org/
    """
    print("--------------- Digest Auth triggered --------------------")
    # only post is authorized
    if request.method == 'POST':
        # get the authorization field
        authorization_field_value=request.headers['authorization']
        print("[Authorization header field]:"+authorization_field_value)
        #############
        #
        # TODO
        #
        #############
        ## This return if success
        #return render_template('auth/successAuth.html')

    ## This return if failure occured
    return render_template('auth/login.html')

@bp.route('/checktoken', methods=('GET', 'POST'))
def checkT():
    """
        EndPoint to check User token validity
        token must be placed on web browser cookies
    """
    #############
    #
    # TODO
    #
    #############
    # si token validé
    #return render_template('auth/successAuth.html')
    
    print (" token not available please log.....") 
    return render_template('auth/login.html')
    

def init_cryto_content():
    if not hasattr(g, 'server_key' ):
        g.block_size=16
        g.server_key=generate_server_key( g.block_size)
        g.vi=generate_VI( g.block_size)
        #g.server_key=get_random_bytes( g.block_size)
        #g.vi=get_random_bytes( g.block_size)
        print("server key:"+str(g.server_key)+", vi "+str(g.vi))