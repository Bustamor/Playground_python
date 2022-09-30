from dataclasses import dataclass
from turtle import bgcolor, color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')``
def index():
    return render_template('index.html')

@app.route('/play')
def three_box():
    data = {
        'num': 3,
        'color': 'purple'
    }
    return render_template("index.html", data = data)


@app.route('/play/<int:num>')
def more_boxes(num):
    data = {
        'num': num,
        'color': 'orange'
    }
    return render_template("index.html", data = data, num = num)

@app.route('/play/<int:num>/<color>')
def new_boxes(num,color):
    data = {
        'num': num,
        'color' : color,   
    }
    return render_template("index.html", data = data, num = num)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)