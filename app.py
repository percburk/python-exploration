from flask import Flask, request, jsonify
import psycopg2

# Initialize app
app = Flask(__name__)

conn = psychopg2.connect("dbname=python_exploration user=kevinburk")
cur = conn.cursor()

cur.execute("SELECT * FROM name_list")

records = cur.fetchall()

# class NameList(Base):
#     __tablename__ = 'name_list'

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String())
#     last_name = db.Column(db.String())
#     age = db.Column(db.Integer)

#     def __init__(first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def one_requests():
    if request.method == 'GET':
        return jsonify(test_data)
    elif request.method == 'POST':
        return 'Made a POST request'
    elif request.method == 'PUT':
        return 'Made a PUT request'
    elif request.method == 'DELETE':
        return 'Made a DELETE request'


test_data = [1, 2, 3, 4]


# Run server
if __name__ == '__main__':
    app.run(debug=True)
