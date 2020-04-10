#!flask/bin/python
import functools
import json
from web_server.tools.keycloak_utils import get_admin,get_oidc,get_token,check_token,create_user
import requests

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,make_response,current_app
)

bp = Blueprint('authkeycloak', __name__, url_prefix='/authkeycloak')


@bp.route('/login',methods=(['POST']))
def login():
    """
        EndPoint for login an User:
        Delegate the login check to keycloak, get back an auth token from keycloak
    """
    #############
    #
    # TODO
    #
    #############
    ## This return if success
    #    response = make_response(render_template("auth/successAuth.html"))
    #    ...
    #    return response

    return render_template('auth/login.html')

@bp.route('/checktoken',methods=('GET','POST'))
def checkToken():
    """
        EndPoint for Checking a user TOKEN:
        Delegate the check to the KeyCloak server
        CAUTION --  to check a tokent your Client should be 'Confidential' and not public so the CLIENT_SECRET should also be set
    """
    #############
    #
    # TODO
    #
    #############
    ## This return if success
    #    return render_template("auth/successAuth.html")
    return render_template('auth/login.html')

@bp.route('/users',methods=(['POST']))
def addUser():
    """
        Endpoint for adding a User into the remote server Keycloak
        User is sent into the request body into json format
    """
    #############
    #
    # TODO
    #
    #############
    return render_template('auth/login.html')


