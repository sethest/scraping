from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/user/<name>')
def user(name):
    return render_template('user15.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
