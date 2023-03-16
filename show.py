from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)

@app.route("/")
def home():
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='mydatabase')
    cursor = cnx.cursor()

    # Fetch data from the database
    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()

    # Render the HTML template with the data
    return render_template('home.html', data=data)

if __name__ == "__main__":
    app.run()
