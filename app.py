from flask import Flask
from flask import request

from functions import is_number

app = Flask(__name__)

# import the math module 
import math 

@app.route("/", methods=['GET'])
def root():
    print('PRIVET VIOLETTA')
    return '<h1>PRIVET VIOLETTA</h1> <img src="https://i.stack.imgur.com/cP8pZ.jpg?s=64&g=1"/>'

# curl -d '{"input1": 1, "input2": 2, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
@app.route("/calculator", methods=['POST'])
def calculator():
    
    json = request.get_json()
    allowed_operators = ['+', '-', '*', '/']
    allowed_json_keys = ['input1', 'input2', 'operator']
    
    # curl -d '{"input2": 1, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # curl -d '{"input1": 1, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # curl -d '{"input1": 1, "input2": 1}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    for key in allowed_json_keys:
        if key not in json:
            return 'Bad request. Error: 1\n'
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    op1 = json['input1']
    op2 = json['input2']
    operator = json['operator']
        
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    for operand in [op1, op2]:
        if isinstance(operand, int) or isinstance(operand, float):
            continue
        if not is_number(operand):
            return 'Bad request. Error: 10\n'
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    # # curl -d '{"input1": "^", "input2": 2, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # if not isinstance(op1, float):
    #     return 'Bad request. Error: 2\n'
    
    # # curl -d '{"input1": 1, "input2": '&', "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # if not isinstance(op2, float):
    #     return 'Bad request. Error: 3\n'
    
    # curl -d '{"input1": 1, "input2": 2, "operator": "sqrt"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    if operator not in allowed_operators:
        return 'Bad request. Error: 4\n'
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    # curl -d '{"input1": 1, "input2": 2, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    if operator == '+':
        return str(float(op1) + float(op2)) + '\n'
    
    # curl -d '{"input1": 1, "input2": 2, "operator": "-"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    elif operator == '-':
        return str(float(op1) - float(op2)) + '\n'
    
    # curl -d '{"input1": 1000000, "input2": 1000000, "operator": "*"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    elif operator == '*':
        return str(float(op1) * float(op2)) + '\n'
    
    # curl -d '{"input1": 100, "input2": 50, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    elif operator == '/':
        return str(float(op1) / float(op2)) + '\n'
    
    # curl -d '{"input1": 100, "input2": 50, "operator": "**"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # curl -d '{"input1": "100", "input2": "50", "operator": "**"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    #elif operator == '**':
       # return str(float(op1) ** float(op2)) + '\n'
    # curl -d '{"input1": 100, "input2": 50, "operator": "100"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    #elif operator == '100':
       # return str((float(op1) + float(op2))* 100 )  + '\n'
    # curl -d '{"input1": 100, "input2": 50, "operator": "sqrt"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    #elif operator == 'sqrt':
       # return str(math.sqrt((float(op1) + float(op2)))) + '\n'
    else:
        return 'Bad request\n'