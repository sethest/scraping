# 在 flask application 內回傳 abort 物件
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route('/user/<uid>')
def get_user(uid):
    if uid == 'root':
        abort(404)

    return '<h1>Hello, {}'.format(uid)


if __name__ == '__main__':
    app.run(debug=True)
