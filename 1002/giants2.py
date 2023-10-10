from flask import Flask, request, render_template, jsonify
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join_post():
    pid = request.form['pid']
    pname = request.form['pname']
    pposition = request.form['pposition']
    pdate = request.form['pdate']
    pgrade = request.form['pgrade']
    
    conn = pymysql.connect(host='localhost', user='aaa', password='1234', db='aaa_db')
    cur = conn.cursor()
    
    sql = "insert into giants_player values (%s, %s, %s, %s, %s);"
    data = (pid, pname, pposition, pdate, pgrade)
    
    cur.execute(sql, data)
    
    conn.commit()
    conn.close()
    
    return jsonify({'msg':'등록 완료!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0")