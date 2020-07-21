# 在 flask application 內回傳 response 物件的 cookie
from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1> A page with cookie </h1>')
    response.set_cookie('answer', '12')
    return response


if __name__ == '__main__':
    app.run(debug='True')
