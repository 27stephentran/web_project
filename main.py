from flask import Flask, render_template, request

app  = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input_page", methods = ["GET", "POST"])
def input_page():
    if request.method == "POST":
        days_off = request.form.get("d-off")
        if request.form.get("l-travel") == "True":
            long_travel_option = request.form.get("long-travel-options")
            other_interest = request.form.get("long-travel-other")
            budget = request.form.get("budget")
            people = request.form.get("people")
            print(days_off, long_travel_option, other_interest, budget, people)
            
        else:
            short_travel_option = request.form.get("short-travel-options")
            other_interest = request.form.get("short-travel-other")
            budget = request.form.get("budget")
            people = request.form.get("people")
            print(days_off, short_travel_option, other_interest, budget, people)
            
    return render_template("input_page.html")






if __name__ == "__main__":
    app.run()
    