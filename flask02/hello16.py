# 用 url_for 生成 URL, 來做 redirect, 不要用 hard code URL
# 否則 @app.route URL 變動, 所有的 redirect URL 都要修改
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index16.html")


@app.route('/login/')
def login():
    # redirect_url = url_for('index')  # 用法一
    # redirect_url = url_for('index', _external=True)  # 用法二
    # redirect_url = url_for('auth', is_login=1, uid=302, uname='login', _external=True)  # 用法三(絕對路徑)
    redirect_url = url_for('auth', is_login=1, uid=302, uname='login')  # 用法三(相對路徑)
    print('==================== WOW ==========================>    ' + redirect_url)
    return redirect(redirect_url)
    return '<h1>Assert: This is login page, but you can\'t see.</h1>'


@app.route('/auth/<is_login>/')
def auth(is_login):
    if is_login == '1':
        uid = request.args.get('uid', default=999, type=int)
        uname = request.args.get('uname', default='***', type=str)
        return '<h1>This is auth page</h1> ' \
               '<h2>Are you = ' + uname + ' ? </h2> ' \
                                          '<h2>Is uid = ' + str(uid) + ' ? </h2>'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
