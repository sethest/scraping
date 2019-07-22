# render_template 範例
# placeholder variables 使用方式

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index01.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user01.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
