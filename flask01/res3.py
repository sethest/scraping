# 在 flask application 內回傳 redirect 物件
# 比較只回傳 response 物件的 status 屬性
from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1> A page with cookie </h1>')
    response.set_cookie('answer', '12')
    return response

@app.route('/response/status')
def response_status():
    response = make_response('<h1> A page with cookie </h1>')
    return response.status

if __name__ == '__main__':
    app.run(debug='True')
