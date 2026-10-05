from flask import Flask,render_template,request,redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)

@app.route("/logout")
def logout():
    name = ''
    id= ''
    msg = 'Logged Out Successfully'
    return render_template('login.html',msg=msg,name=name,id=id)


@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='4272',
            database='Login'
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE username = %s AND password = %s', (username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successful')
            return render_template('welcome.html', msg=msg, name=name, id=id)
        else:
            msg = 'incorrect Credentials. Kindly check'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')


app.run(debug=True)