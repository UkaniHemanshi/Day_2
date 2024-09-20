from flask import Flask, request, render_template,redirect,url_for

#1. Initialize Flask app
appsurvey = Flask(__name__)
print(appsurvey)

@appsurvey.route('/')
def home():
    return render_template('home.html')

@appsurvey.route('/surveyform')
def surveytaken():
    return render_template('survey.html')


@appsurvey.route('/surveyresult',methods=['POST'])
def survey_details():
    name = request.form['name']
    print(name)
    return render_template("results.html",name1 = name)


if __name__ == '__main__':
    appsurvey.run(debug=True,port=5001)