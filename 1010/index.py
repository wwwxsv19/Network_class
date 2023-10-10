from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import connectDB

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/on")
def led_on():
    try:
        GPIO.output(8, GPIO.HIGH)
        connectDB.insertStatus('on')
        return "ok"
    except:
        return "fail"

@app.route("/off")
def led_off():
    try:
        GPIO.output(8, GPIO.LOW)
        connectDB.insertStatus('off')
        return "ok"
    except:
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0")