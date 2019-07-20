# 在 flask application 內回傳 response 物件
# 回傳一個 http status code 400
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400


if __name__ == '__main__':
    app.run(debug=True)


