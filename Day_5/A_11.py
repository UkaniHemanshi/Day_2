import csv

data = [
    {'Name': 'Nikhil', 'ID': 108, 'Age': 21, 'Grade': 9.0},
    {'Name': 'Sanchit', 'ID': 107, 'Age': 22, 'Grade': 9.1},
    {'Name': 'Aditya', 'ID': 103, 'Age': 23, 'Grade': 9.3},
    {'Name': 'Sagar', 'ID': 102, 'Age': 19, 'Grade': 9.5},
    {'Name': 'Prateek', 'ID': 180, 'Age': 30, 'Grade': 7.8},
    {'Name': 'Sahil', 'ID': 101, 'Age': 20, 'Grade': 9.1}
]

with open('student_records.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID','Name','Age', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
def read_csv_file(filename : str):


read_csv_file(filename='student_records.csv')
