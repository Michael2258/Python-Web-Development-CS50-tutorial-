from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  names = ["Irene", "Seulgi", "Wendy", "Joy", "Yeri"]
  return render_template("index.html", names=names)

@app.route("/more")
def more():
  others = ["Suho", "Taeyeon", "Sakura"]
  return render_template("more.html", others=others)

if __name__ == "__main__":
    app.run()