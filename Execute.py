from Solver import *
from flask import Flask, render_template, request
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER']="uploads"

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        eqn=request.files["eqn"]
        path = os.path.join(app.config['UPLOAD_FOLDER'], eqn.filename)
        eqn.save(path)
        return render_template("final.html", equation=read(path), answer=eval(read(path)))
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run()