# -*- coding: utf-8 -*-

"""

author: Karla Elena Pelaez Cruz

"""

from server import app
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


from flask import render_template, request, session, flash, url_for, redirect, jsonify, make_response
from werkzeug.security import check_password_hash
from functools import wraps
import re
import datetime

from server import app


@app.route('/api/encrypt_bss', methods=['POST'])
def encrypt_data():

    if 'str_data' in request.args:
        str_data = request.args['str_data']

    if 'ambiente' in request.args:
        ambiente = request.args['ambiente']
    else:
        ambiente = 'TEST'

    key = app.config['BSS_KEY_' + ambiente]

    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    padded_text = pad(str_data.encode('utf-8'))

    iv = Random.new().read(AES.block_size)

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)

    encrypted_text = cipher.encrypt(padded_text)

    concat_text = iv + encrypted_text

    result = b64encode(concat_text).decode('utf-8')

    return result


@app.route('/api/decrypt_bss', methods=['POST'])
def decrypt_data():

    if 'encrypted_data' in request.args:
        encrypted_data = request.args['encrypted_data']
    if 'ambiente' in request.args:
        ambiente = request.args['ambiente']
    else:
        ambiente = 'TEST'

    key = app.config['BSS_KEY_' + ambiente]

    unpad = lambda s: s[0:-ord(s[-1])]

    data = b64decode(encrypted_data.encode('utf-8'))

    iv = data[:16]
    enc = data[16:]

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)

    decrypted_data = cipher.decrypt(enc)

    result = unpad(decrypted_data)

    return result
