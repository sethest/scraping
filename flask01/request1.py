# 在 flask application 內取得 request 的內容

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('user-agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


if __name__ == '__main__':
    app.run(debug=True)
