from flask import Flask, request, render_template,redirect,url_for

#1. Initialize Flask app
appLogin = Flask(__name__)
print(appLogin)

#2. Create a route for the login page
@appLogin.route('/')
def  login():
    return render_template('login.html')

#3. create a route to handle the login form submission
@appLogin.route('/login',methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    #4. Simple username and password authentication
    if username =="admin" and password == "password":
        # return f"Welcome{username}"
        return redirect(url_for('show_dashboard'))
    else :
        return "Invalid credentials"

@appLogin.route('/Dashboard')
def show_dashboard():
    return render_template("Dashboard.html")

#5. Run the flask app
if __name__ == '__main__':
    appLogin.run(debug=True,port=5001)