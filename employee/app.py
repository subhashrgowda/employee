import sys

from flask import Flask, render_template, request, jsonify
#from flask_mysqldb import MySQL
import mysql.connector
app = Flask(__name__)

# MySQL configurations
'''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'employee_db'''

cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='employee_db')


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    try:
        # Get data from the request
        data = request.get_json()
        name = data['name']
        position = data['position']
        print(name , position , file = sys.stdout)
        # Insert data into the database
        cur = cnx.cursor()
        cur.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", (name, position))
        cnx.commit()

        cur.close()

        return jsonify(success=True)
    except Exception as e:
        print(str(e))
        return jsonify(success=False)

@app.route('/get_employees')
def get_employees():
    try:
        # Fetch data from the database
        cur = cnx.cursor()
        cur.execute("SELECT name, position FROM employees")
        data = cur.fetchall()
        cur.close()


        # Convert data to a list of dictionaries
        employees = [{'name': row[0], 'position': row[1]} for row in data]

        return jsonify(employees)
    except Exception as e:
        print(str(e))
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
