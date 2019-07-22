# Jinja2可接收各種型態的 placeholder variable

from flask import Flask
from flask import render_template

app = Flask(__name__)


class Circle:
    def __init__(self, r=0):
        self.radius = r

    def AREA(self):
        return self.radius * self.radius * 3.14


@app.route('/')
def index():
    this_dict = {'a': 1, 2: "qqqqq", 'key': 3}
    this_list = [1, 2, 3, 4, 5]
    this_index = 2
    this_object = Circle(10)

    return render_template("index02.html",
                           mydict=this_dict,
                           mylist=this_list,
                           myindex=this_index,
                           myobject=this_object)


if __name__ == '__main__':
    app.run(debug=True)
