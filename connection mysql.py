from flask import Flask, jsonify, request
from flask_mysqldb import MySQL



app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_HOST'] = 'localhost'


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM computer''')
    rv = cur.fetchall()
    return jsonify({'data': rv}), 201

if __name__ == '__main__':
    app.run(debug=True)
