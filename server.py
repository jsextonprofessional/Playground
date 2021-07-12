from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play/")
def box_generator_starter():
    return render_template("index.html", num = 3, color = "lightblue")

@app.route("/play/<int:num>/")
def box_generator_number(num):
    return render_template("index.html", num = num, color = "lightblue")

@app.route("/play/<int:num>/<string:color>")
def box_generator_color(num, color):
    return render_template("index.html", num = num, color = color)
    
if __name__=="__main__":
    app.run(debug=True)