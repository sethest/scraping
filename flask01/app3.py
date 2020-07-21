# 動態路徑 : int形態的範例
# 開啟瀏覽器到 http://localhost:5000/number/123/111
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {}</h1>'.format(name)


# 加入以下的route，動態部分為int
@app.route('/number/<int:num1>/<int:num2>')
def number(num1, num2):
    return '<h1>{} + {} = {}</h1>'.format(num1, num2, num1+num2)


if __name__ == '__main__':
    app.run(debug=True)
