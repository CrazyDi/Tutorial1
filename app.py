from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    data_dict = request.get_json()
    x = data_dict["x"]
    y = data_dict["y"]
    z = x + y

    res = {"z": z}
    return jsonify(res), 200


if __name__ == '__main__':
    app.run()
