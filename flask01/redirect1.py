# 在 flask application 內回傳 redirect 物件
from flask import Flask
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://www.yzu.edu.tw/')


if __name__ == '__main__':
    app.run(debug=True)
