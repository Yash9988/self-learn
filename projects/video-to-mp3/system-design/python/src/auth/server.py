import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL


server = Flask(__name__)
mysql = MySQL(server)

# Config
mysql.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
