# Jinja2 支持流程控制語法: if 範例

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    this_user = None   # this_user = ""
    return render_template('index05.html', user=this_user)

if __name__ == '__main__':
    app.run(debug=True)