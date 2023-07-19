from flask import Flask,request
import sqlite3

con = sqlite3.connect('user_db.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user (user_id TEXT, password TEXT)")
con.commit()
con.close()


app = Flask(__name__)

@app.route('/') #endpoint
def home():
    return "Welcome"

# signup
@app.route('/signup', methods = ['POST']) #endpoint
def signup():
    data = request.get_json()
    con = sqlite3.connect('user_db.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO user  VALUES ('{}','{}')""".format(data['user_id'],
                                                              data['password']))
    con.commit()
    con.close()
    return "User id has been created"

# login
@app.route('/login', methods = ['POST']) #endpoint
def login():
    data = request.get_json()
    con = sqlite3.connect('user_db.db')
    cur = con.cursor()
    data1 = cur.execute("""SELECT * from user WHERE user_id = '{}' and password = '{}' """.format(data['user_id'],
                                                                                                  data['password']))
    print(data1)
    db_data = cur.fetchall()
    print(db_data)
    con.commit()
    con.close()
    if len(db_data)>=1:
        return " Logged in successfully..."
    else:
        return "Incorrect user id or password, try again..."

# showall
@app.route('/showall')
def showall():
    con = sqlite3.connect('user_db.db')
    cur = con.cursor()
    data1 = cur.execute("""SELECT * from user  """)
    db_data = cur.fetchall()
    con.commit()
    con.close()
    return db_data


# update
# delete


app.run()