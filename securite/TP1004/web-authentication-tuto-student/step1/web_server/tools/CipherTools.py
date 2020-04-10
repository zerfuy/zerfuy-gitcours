import functools
import base64
import binascii
import re
import hashlib
#pip install pycryptodome
#from Crypto.Cipher import AES
import random
import time
import uuid
# from Crypto.Util.Padding import pad,unpad
#from Crypto.Random import get_random_bytes
import json
import numpy as np
import copy


def computeHashDIgest(method,uri,username,realm,nonce,pwd):
    resulted_auth_digest=""
    #############
    #
    # TODO
    #
    #############
    return resulted_auth_digest

def generateTokenSHA256(username,key):
    """ Generate a token given a username, token is signed in SHA256
        @param username: name to add to the token
        @param key: secret to add to the signature
    """
    my_signed_token={}
    #############
    #
    # TODO
    #
    #############
    return my_signed_token


def checkTokenSHA256(key,token_received):
    """ Check if a generated token is valid or note 
        @param token_received: the token to check (including its signature)
        @param key: secret to add to the signature
    """
    token=copy.deepcopy(token_received)
    print("FCT checkTokenSHA256: token:")
    print(token)
    #############
    #
    # TODO
    #
    #############
    return False

def generate_server_key(size):
    """Generate a random key according the given size
        @param size: size of the key CAUTION must be complite with the encryption algorithm (16, 64, 128)
    """
    #key = ''.join(chr(random.randint(0, 0xFF)) for i in range(size))
    key =np.random.bytes(size)
    return key


    
def generate_VI(size):
    """Generate a initialization vector for encryption algorithm
        @param size: size of the key CAUTION must be complite with the encryption algorithm (16, 64, 128)
    """
    #vi = ''.join([chr(random.randint(0, 0xFF)) for i in range(size)])
    vi =np.random.bytes(size)
    return vi