from flask import Flask, render_template

app  = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input_page")
def input_page():
    return render_template("input_page.html")


if __name__ == "__main__":
    app.run()
    