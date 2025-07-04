from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    love_percentage = None
    male_name = ''
    female_name = ''
    if request.method == 'POST':
        male_name = request.form['male_name']
        female_name = request.form['female_name']
        if male_name and female_name:
            random.seed(male_name + female_name)
            love_percentage = random.randint(50, 100)  # 50% से 100% के बीच
    return render_template('index.html', love=love_percentage, male_name=male_name, female_name=female_name)

if __name__ == '__main__':
    app.run(debug=True)