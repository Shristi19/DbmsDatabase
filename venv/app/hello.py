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
    return render_template('login.html',message="")


@app.route('/Authenticate', methods = ['POST','GET'])
def Authenticate():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return render_template('result.html', message=message)




if __name__ == "__main__":
    app.run(debug=True)