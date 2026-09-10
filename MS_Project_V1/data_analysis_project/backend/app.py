from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello Flask!"


@app.route("/test")
def test():
    name = request.args.get("name")
    return "参数是" + name


@app.route("/post_test", methods=["POST"])
def post_test():
    data = request.json
    name = data.get("name")
    return "body中的参数是" + name


@app.route("/test2", methods=["POST"])
def test2():

    # 获取 POST Body
    body_data = request.json

    # 获取 Body 里面的参数
    body_value = body_data.get("body")

    # 获取 URL 参数
    param_value = request.args.get("param")

    # 获取 URL 中的第三个参数
    age_value = request.args.get("age")

    return "body中的参数是" + body_value + "，param中的参数是" + param_value + "，第三个参数是" + age_value


if __name__ == "__main__":
    app.run(debug=True)