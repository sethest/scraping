# 使用 numpy(np) 資料型態
# 類似建立模板語法的函式

from flask import Flask
from flask import render_template
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    return render_template('index12.html', myTable=a)


if __name__ == '__main__':
    app.run(debug=True)
