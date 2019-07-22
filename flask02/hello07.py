# Jinja2 支持流程控制語法: for 範例

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    this_list = [1, 22, 333, 4444, 5555]
    return render_template('index07.html', items=this_list)

if __name__ == '__main__':
    app.run(debug=True)