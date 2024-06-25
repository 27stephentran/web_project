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
            long_travel = "True"
            long_travel_option = request.form.get("long-travel-options")
            other_interest = request.form.get("long-travel-other")
            budget = request.form.get("budget")
            people = request.form.get("people")
            plan = generate_plan(days_off, long_travel, long_travel_option, other_interest, budget, people)
            print(days_off, long_travel, long_travel_option, other_interest, budget, people)
            
            
        else:
            long_travel = "False"
            short_travel_option = request.form.get("short-travel-options")
            other_interest = request.form.get("short-travel-other")
            budget = request.form.get("budget")
            people = request.form.get("people")
            plan = generate_plan(days_off, long_travel, short_travel_option, other_interest, budget, people)
        
        return render_template("recommendation.html", recommendations = plan)
    return render_template("input_page.html")

@app.route("/recommendation")
def recomendation():
    return render_template("recommendation.html")

def generate_plan(days_off, long_travel, travel_option, other_interest, budget, people):
    html_content = '''
    <h1> Here is our recomendation based on your choices</h1>
    '''

    long_travel_plan = {
        "Nha-trang" : {
            "Day 01": [["LONG SON PAGODA WITH WHITE BUDDHA"], 
                       ["HON CHONG ROCKS"], 
                       ["NATIONAL OCEANOGRAPHIC MUSEUM"]],
            "Day 02": [["NHA TRANG CATHEDRAL"], 
                       ["THE BEACHE"], 
                       ["FESTIVALS IN NHA TRANG"]]
        },
        "Option-2" : {
            "Day 01": [["Activity 01"],
                       ["Activity 02"],
                       ["Activity 03"]],

            "Day 02" : [["Activity 04"],
                       ["Activity 05"],
                       ["Activity 06"]],
        },
        "Option-3" : {
            "Day 01": [["Activity 01"],
                       ["Activity 02"],
                       ["Activity 03"]],

            "Day 02" : [["Activity 04"],
                       ["Activity 05"],
                       ["Activity 06"]],
        }
    }
    if long_travel == "True":
        place = long_travel_plan[travel_option] 
        activities = []
        for day in place:
            activities.append(place[day])
        
        html_content += '<table border = "1" color = "red">'
        for day in range(int(days_off)):
            day_key = f"Day {day + 1:02}"
            if day_key in place:
                activities = place[day_key]
                html_content += f'<tr><th colspan="3">Day {day + 1}</th></tr>'

                parts_of_day = ["Morning", "Afternoon", "Evening"]
                for part, activity in zip(parts_of_day, activities):
                    html_content += f'<tr><td>{part}:</td>'
                    activity_detail = activity[0]
                    html_content += f'<td colspan="2">{activity_detail}</td></tr>'
            else:
                break
        html_content += "</table>"



    return html_content









if __name__ == "__main__":
    app.run()
    