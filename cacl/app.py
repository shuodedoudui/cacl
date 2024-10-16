from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operator = request.form['operator']

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "无效的输入"

    result = None
    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "除数不能为零"
    elif operator == 'sin':
        angle_degrees = num1
        angle_radians = math.radians(angle_degrees)
        result = math.sin(angle_radians)
    elif operator == 'cos':
        angle_degrees = num1
        angle_radians = math.radians(angle_degrees)
        result = math.cos(angle_radians)
    elif operator == 'tan':
        angle_degrees = num1
        angle_radians = math.radians(angle_degrees)
        result = math.tan(angle_radians)
    elif operator == 'cot':
        angle_degrees = num1
        angle_radians = math.radians(angle_degrees)
        result = 1 / math.tan(angle_radians)

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
