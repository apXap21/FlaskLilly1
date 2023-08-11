from flask import Flask, render_template

app = Flask(__name__)
# apoorv
@app.route("/")
def hello_world():
    number=26
    name=[1,2]
    return render_template("index.html",num=number,name=name)


if __name__=="__main__":
    app.run(debug=True)