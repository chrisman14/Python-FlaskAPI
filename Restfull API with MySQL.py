from flask import Flask, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_HOST'] = 'localhost'


class HelloWorld(Resource):
    def get(self):
        return {'about': "Hello World"}

    def post(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM sms_smsbanking_blacklist limit 1000''')
        rv = cur.fetchall()
        return ({'data': rv}), 201


class Multi(Resource):
    def get(self, num):
        return{'result :': num*10}


api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/mulri/<int:num>')


if __name__ == "__main__":
    app.run(debug=True)
