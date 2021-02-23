from flask import Flask, jsonify
app = Flask(__name__)

test_data = [
    {"first name": 'Kevin', "last name": 'Burk'},
    {"first name": 'Travis', "last name": 'Huss'},
    {"first name": 'Dane', "last name": 'Smith'}
]


@app.route('/', methods=['GET'])
def index():
    return jsonify(test_data)


if __name__ == '__main__':
    app.run(debug=True)
