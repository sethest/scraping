# 對 placeholder variable 使用 filter

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    this_str = "    this is a book    "
    this_html = "<ul><li> SOS </li></ul>"

    return render_template('index04.html',
                           myStr=this_str,
                           myHTML=this_html)


if __name__ == '__main__':
    app.run(debug=True)
