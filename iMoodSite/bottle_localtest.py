# -*- coding: utf-8 -*-
# @Author: imoodmap Group

from bottle import Bottle,run,template,request,debug
import sqlite3


app =Bottle()
@app.route('/')
@app.route('/input/<name>')
def mainpage(name ='imm'):
	return 'hello'

@app.route('/output',method = 'POST')
def output():
    diaryContent =request.forms.get('diaryContent')
    flowValue =request.forms.get('flowValue')
    return template('Your flowValue is {{number}}, and your notes are {{notes}}', number = str(flowValue), notes = diaryContent)

from bottle import static_file
@app.route('/static/header-bg.jpg')
def server_static(header-bg.jpg):
    return "static_file(header-bg.jpg, root='static')"

debug(True)
run(app, host='localhost', port =8080,reloader=True)
