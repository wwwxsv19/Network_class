from flask import Flask, request, render_template

import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<num>")
def up(num):
    conn = pymysql.connect(host='localhost', user='aaa', password='1234', db='aaa_db')
    cur = conn.cursor()
    sql = "insert into numcount values (%s)"
    data = num
    cur.execute(sql, data)
    conn.commit()
    conn.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")