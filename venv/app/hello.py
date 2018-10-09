from flask import Flask
import pymysql as sql
from flask import Flask, flash, redirect, render_template, request, session, abort,redirect
import os
import pymysql as sql
conn=sql.connect(host='localhost',port=3306,user='root',password='root123',db='DbmsProject')
cursor=conn.cursor();
app = Flask(__name__)


"""@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@app.route("/Authenticate", methods=['POST'])
def Authenticate():
    if request.form['username']=='admin' and request.form['password'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()
    """

@app.route('/')
def index():
    return render_template('login.html')

#import pymysql as sql
#import flask

@app.route('/Authenticate', methods = ['POST','GET'])
def Authenticate():
    message =''
    if request.method == 'POST':
        user = request.form['username'] # access the data inside
        pwd = request.form['password']

        conn = sql.connect(host='localhost', port=3306, user='root', password='root123', db='DbmsProject')
        cursor = conn.cursor();
        cursor.execute("SELECT Password FROM examples WHERE Username = username ")
        result = (cursor.fetchall()[0][0])
        print(result)
        print(pwd)

        if(result == pwd):
            return render_template('result.html',message="Correct")
        else:
            return render_template('result.html', message="Wrong")
        # print(cursor
        #      .fetchall())

        #if username == 'result' and password == '':
         #   message = "Correct username and password"
        #else:
         #   message = "Wrong username or password"






if __name__ == "__main__":
    app.run(debug=True)
