from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from HTML form
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    mobile = request.form['mobile'] 
    role= request.form['role']
    
    
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )
    
    # Insert data into MySQL table
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, email, age, mobile, role) VALUES (%s, %s, %s, %s,%s)"
    val = (name, email, age, mobile, role)
    mycursor.execute(sql, val)
    mydb.commit()
    
    # Render success page
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
