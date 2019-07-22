# Jinja2 在 rendering 會將 placeholder variable 內的特殊字元轉成對應代碼
# 避免 HTML injection (XSS)
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    this_html = '<ul><li> SOS.</li></ul>'
    return render_template('index03.html', myHTML=this_html)

if __name__ == '__main__':
    app.run(debug=True)