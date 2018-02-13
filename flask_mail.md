"""
# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
	MAIL_SERVER='smtp.163.com',
	MAIL_PORT='465',
	MAIL_USE_SSL=True,
	MAIL_USERNAME='dbwatcher@163.com',
	MAIL_PASSWORD='xxxxxxxx'
	)

mail = Mail(app)

@app.route('/')
def index():
	msg = Message(subject="MySQL report", sender='@163.com', recipients=['@163.com'])
	msg.html='<h1>MySQL Backup info！</h1>'
	mail.send(msg)
	return "MySQL infor"

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
"""
