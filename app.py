from flask import Flask,request,jsonify,render_template
app= Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")



@app.route("/operation",methods=["POST"])
def math_operation():
    if request.method=="POST":
        operation=request.form["operation"]
        num1=int(request.form["num1"])
        num2=int(request.form["num2"])
        if operation=="add":
            result=num1+num2
        elif operation=="subtract":
            result=num1-num2
        elif operation=="multiply":
            result=num1*num2
        else:
            result=num1/num2
        return render_template('results.html',result=result)
    else:
        return "thius is not correct"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)
