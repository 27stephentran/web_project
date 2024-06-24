from flask import Flask, render_template, request
from functionalities import input_handle
import random
app = Flask(__name__)

morning_activities = ["art galleries", "museums", "beaches"]
afternoon_activities = ["resorts", "parks picnic spots", "theaters", "juice bars"]
evening_activities = ["dance clubs", "juice bars", "restaurants", "theaters"]
activities = [morning_activities, afternoon_activities, evening_activities]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_page', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        days_off = request.form.get('days_off')
        long_travel = request.form.get('long_travel')
        type_of_prefer = request.form.getlist('type_of_prefer')
        budget = request.form.get('budget')

        checkbox_data = input_handle.process_checkbox_data(type_of_prefer)
        recommendation_html = generate_html(days_off, long_travel, type_of_prefer, budget, checkbox_data)

        # Pass recommendation HTML to the template
        return render_template('recommendation.html', recommendation=recommendation_html)
    else:
        return render_template('predict_page.html')

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

def generate_html(days_off, long_travel, type_of_prefer, budget, checkbox_data):
    html_content = '''
    <h1>Here is our recommendation based on your selections</h1>
    '''

    # List of places
    places = {
        "Morning": {
            "DIY": "A DIY workshop",
            "art galleries": "An art museum"
        },
        "Afternoon": {
            "beach": "A relaxing time at the beach",
            "hiking": "A scenic hiking trail"
        },
        "Evening": {
            "restaurant": "A fine dining experience",
            "theater": "A theater performance"
        }
    }

    # Filter out activities based on checkbox_data
    available_activities = {part: [] for part in ["Morning", "Afternoon", "Evening"]}
    for activity in type_of_prefer:
        for part_of_day, activities in places.items():
            if checkbox_data.get(activity, False) and activity in activities:
                available_activities[part_of_day].append(places[part_of_day][activity])

    html_content += '<table border="1" color = "red">'

    for day in range(int(days_off)):
        html_content += f'''
        <tr><th colspan="3">Day {day + 1}</th></tr>
        '''
        
        parts_of_day = ['Morning', 'Afternoon', 'Evening']
        for part_of_day in parts_of_day:
            html_content += f'<tr><td>{part_of_day}:</td>'
            
            if available_activities[part_of_day]:
                activity = random.choice(available_activities[part_of_day])
                html_content += f'<td colspan="2">{activity}</td>'
                # Remove the selected activity to ensure it's not repeated
                available_activities[part_of_day].remove(activity)
            else:
                html_content += '<td colspan="2">Relax at home</td>'
            
            html_content += '</tr>'
    
    html_content += '</table>'
    
    return html_content




# def generate_html(days_off, long_travel, type_of_prefer, budget, checkbox_data):
#     html_content = '''
#     <h1>Here is our recommendation based on your selections</h1>
#     '''

#     # Filter out activities based on checkbox_data
#     available_activities = [activity for activity in type_of_prefer if checkbox_data.get(activity, False)]
#     parts_of_day = ['Morning', 'Afternoon', 'Evening']
#     for day in range(int(days_off)):
#         html_content += f'''
#         <h2>Day {day + 1}</h2>
#         '''
#         html_content += '<table border="1">'
        
        
#         # Morning, Afternoon, Evening
#         for part_of_day in parts_of_day:
#             html_content += f'<tr><td>{part_of_day}:</td>'
#             possible_activities = activities[parts_of_day.index(part_of_day)]
#             # Pick a random activity for the part of the day
#             if available_activities:
#                 for available in available_activities:
#                     if available in possible_activities:
#                         html_content += f'<td>{available}</td>'

                
#                 html_content += "</tr>"
#         html_content += "</table>"
    
#     return html_content



if __name__ == '__main__':
    app.run(debug=True)