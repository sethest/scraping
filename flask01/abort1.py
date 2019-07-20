# 在 flask application 內回傳 abort 物件
from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route('/user/<id>')
def get_user(id):
    if id == 'qqq':
        abort(404)
    return '<h1>Hello, {}'.format(id)

if __name__ == '__main__':
    app.run(debug=True)