from flask import Flask, request, render_template,redirect,url_for

#1. Initialize Flask app
appAgeChecker = Flask(__name__)
print(appAgeChecker)

@appAgeChecker.route('/')
def home():
    return render_template('home.html')

@appAgeChecker.route('/Ageform')
def AgeChecker():
    return render_template('Ageform.html')


@appAgeChecker.route('/Agecheck',methods=['POST'])
def Ageform():
    name = request.form['name']
    age = int(request.form['age'])

    if age >= 18:
        return redirect(url_for('result_dashboard'))
    else :
        return "You are a Minor"

@appAgeChecker.route('/Result')
def result_dashboard():
    return render_template("Result.html")

if __name__ == '__main__':
    appAgeChecker.run(debug=True,port=5001)