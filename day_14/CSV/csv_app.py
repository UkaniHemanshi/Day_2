from flask import Flask, request, render_template,redirect,url_for,session
import pandas as pd

appcsv = Flask(__name__)
appcsv.secret_key = 'secret'
print(appcsv)

@appcsv.route('/')
def home():
    return render_template('csvform.html')

@appcsv.route('/csvdata',methods=['POST'])
def product():
    list = []
    csv_path = request.form['path']
    df = pd.read_csv(csv_path)
    for column_name in df.columns:
        list.append(column_name)
    session['Header'] = list

    return redirect(url_for('csv_to_dataframe'))

@appcsv.route('/csvdata')
def csv_to_dataframe():
    column_names = session.get('Header', [])

    return render_template("csv_datatable.html",columns = column_names)


if __name__ == '__main__':
    appcsv.run(debug=True,port=5001)