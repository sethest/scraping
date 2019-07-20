# 動態路徑 : path形態的範例
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {}</h1>'.format(name)


@app.route('/number/<int:num1>/<int:num2>')
def number(num1, num2):
    return '<h1>{} + {} = {}</h1>'.format(num1, num2, num1 + num2)


@app.route('/realNumber/<float:num>')
def realNumber(num):
    return '<h1>{} * 2 = {}</h1>'.format(num, 2 * num)


@app.route('/filepath/<path:path00>')
def filepath(path00):
    return '<h1>Path is {}'.format(path00)


if __name__ == '__main__':
    app.run(debug=True)
