from flask import Flask
from flask_mysqldb import MySQL
import yaml
import os

app=Flask(__name__)

db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
app.config['SECRET_KEY'] = os.urandom(10)


@app.route('/')
def index():
    choice = '5'
    while(choice != '4'):
        print("Movies Data")
        print("1.Insert a Movie")
        print("2.Show all the Movies")
        print("3.Show Movie Based on Actor's Name")
        print("4.Exit")
        choice = input()
        if choice=='1':
            print("Movie Name: ")
            name = input()
            print("Movie Actor: ")
            actor = input()
            print("Movie Actress: ")
            actress = input()
            print("Movie Director: ")
            director = input()
            print("Year of Release: ")
            release = input()
            cur = mysql.connection.cursor()
            cur.execute("insert into movie values(%s,%s,%s,%s,%s)",(name,actor,actress,director,release))
            mysql.connection.commit()
        if choice=='2':
            cur = mysql.connection.cursor()
            cur.execute("select * from movie")
            data = cur.fetchall()
            print(data)
        if choice=='3':
            print("Actor name: ")
            f = input()
            cur = mysql.connection.cursor()
            cur.execute(f"select * from movie where actor='{f}'")
            data = cur.fetchall()
            print(data)
    return 0







if __name__=="__main__":
    app.run(debug=True)
