from flask import Flask, request, render_template, jsonify
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join_post():
    pid = request.form['pid']
    conn = pymysql.connect(host='localhost', user='aaa', password='1234', db='aaa_db')
    cur = conn.cursor()
    sql = "insert into numcount values (%s)"
    cur.execute(sql, pid)
    conn.commit()
    conn.close()
    return jsonify({'msg': '등록 완료!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0")