from flask import Flask,render_template



app=Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/signIn")
def signUp():
    return render_template("signIn.html")



if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
    