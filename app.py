from importlib.resources import open_text
from click import open_file
from flask import Flask
from flask import request

from functions import is_number

app = Flask(__name__)

# import the math module 
import math 

@app.route("/", methods=['GET'])
def root():
    print('WEB-API-CALCULTOR-PY')
    
    # Open a file: file
    file = open('README.md',mode='r')
 
    # read all lines at once
    all_of_it = file.read()
 
    # close the file
    file.close()
    print(all_of_it.splitlines())
    return '<br>'.join(all_of_it.splitlines())

   


# curl -d '{"input1": 1, "input2": 2, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
@app.route("/calculator", methods=['POST'])
def calculator():
    #curl -d  -X  http://127.0.0.1:5000/calculator
    #if request.headers['Content-Type'] != 'application/json; charset=UTF-8':
    #     return 'Bad request. JSON required. Error 1\n'
    json = request.get_json()
    allowed_operators = ['+', '-', '*', '/']
    allowed_json_keys = ['input1', 'input2', 'operator']
    
    # curl -d '{"input2": 1, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # curl -d '{"input1": 1, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # curl -d '{"input1": 1, "input2": 1}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    for key in allowed_json_keys:
        if key not in json:
            return 'Bad request. Error: 2\n'
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    op1 = json['input1']
    op2 = json['input2']
    operator = json['operator']
        
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    for operand in [op1, op2]:
        if isinstance(operand, int) or isinstance(operand, float):
            continue
        if not is_number(operand):
            return 'Bad request. Error: 3\n'
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    # curl -d '{"input1": "^", "input2": 2, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    #   if not isinstance(op1, float):
    #       return 'Bad request. Error: n\n'
    
    # curl -d '{"input1": 1, "input2": "&", "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    #   if not isinstance(op2, float):
    #       return 'Bad request. Error: n2\n'
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

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
    else:
        return 'Bad request. Error: 5\n'