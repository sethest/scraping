# 動態路徑 : path形態的範例
# path形態與string形態相同，但允許有’/’在path內。
# 開啟瀏覽器到 http://localhost:5000/filepath/12/3/4/a/bb
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


@app.route('/real_number/<float:num>')
def real_number(num):
    return '<h1>{} * 2 = {}</h1>'.format(num, 2 * num)


# 加入以下的route，動態部分為 path
@app.route('/filepath/<path:path00>')
def filepath(path00):
    return '<h1>Path is {}'.format(path00)


if __name__ == '__main__':
    app.run(debug=True)
