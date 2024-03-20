from flask import Flask, render_template, url_for, request, redirect
from question import DataCollection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template('welcome.html')


@app.route("/information")
def information():
    return render_template('information.html', title='Information')

@app.route("/data_collection", methods=['GET', 'POST'])
def data_collection():
    form = DataCollection()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        student_number = form.student_number.data
        email = form.email.data
        grade = form.grades.data
        satisfication = form.satisfaction.data
        favorite_subject = form.favorite_subject.data
        suggestion = form.suggestions.data
        recommendation = form.recommendations.data
        f = open('data.txt', 'w')
        f.write(f" Name: {first_name} {last_name},\n P Number: {student_number},\n Email: {email},\n Grade: {grade},\n Overall Satisfication: {satisfication},\n Favorite Subject: {favorite_subject},\n Suggestion: {suggestion},\n Recommendation: {recommendation}")
        f.close()
        # Process the
        return redirect('/result')
    return render_template('data-collection.html', title='Data Collection', form=form)

@app.route("/result")
def result():
    return render_template('result.html')
    

if __name__ == '__main__':
    app.run(debug=True)