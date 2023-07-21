from flask import Flask, render_template
import pymssql


app = Flask(__name__)

# SQL Server connection settings
server = '188.42.96.158'
database = 'MOB_Discovery'
username = 'mobdisc'
password = 'mobdisc@123'

conn = pymssql.connect(server=server, database=database, user=username, password=password)


@app.route('/')
def fetch_data():
    # Fetch data from the "mobdiscovery2" table
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logging')
    data = cursor.fetchall()

    # Render the template and pass the data
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
