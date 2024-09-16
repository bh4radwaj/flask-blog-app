#!/usr/bin/python3
import pymysql
import os
import secrets
import subprocess
from flask import Flask,request,redirect,render_template,jsonify,make_response,url_for,flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_ckeditor import CKEditor
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root: @localhost/flask'
app.config['SECRET_KEY'] = ''
db = SQLAlchemy(app)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = ""
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "flask"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
ckeditor = CKEditor(app)

mysql = MySQL(app)

