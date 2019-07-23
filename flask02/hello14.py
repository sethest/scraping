from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/user/<name>')
def user(name):
    return render_template('user14.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
