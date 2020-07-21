# 動態路徑 : String (預設)形態的範例
# 開啟瀏覽器到 http://localhost:5000/user/Mary
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


# 加入以下的route，動態部分為 str(預設)
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
