from flask import Flask, render_template,jsonify, request
from src.prompt import qa


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get" , methods = ["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    return str(result["result"])
    

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)