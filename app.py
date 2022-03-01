from importlib.resources import open_text
from wsgiref import headers
from click import open_file
from flask import Flask
from flask import request

from functions import is_number

app = Flask(__name__)

# import the math module
# import math


@app.route("/", methods=['GET'])
def root():
    print('WEB-API-CALCULTOR-PY')

    # Open a file: file
    file = open('README.md', mode='r')

    # read all lines at once
    all_of_it = file.read()

    # close the file
    file.close()
    print(all_of_it.splitlines())
    return '<br>'.join(all_of_it.splitlines())


# curl -d '{"input1": 1, "input2": 2, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    # 1. https://stackoverflow.com/questions/29386995/how-to-get-http-headers-in-flask
    if 'Content-Type' not in request.headers:
       return '`Content-Type` is required. Error: 1'
    
    # 2. https://stackoverflow.com/questions/23714383/what-are-all-the-possible-values-for-http-content-type-header
    # 2. Encoding
    # if request.headers['Content-Type'] != 'application/json' or request.headers['Content-Type'] != 'application/json; charset=utf-8':
    #     print(request.headers['Content-Type'])
    #     return '`Content-Type` must be `application/json`. Error: 2'
    
    if request.headers['Content-Type'] not in ['application/json', 'application/json; charset=utf-8']:
        return '`Content-Type` must be `application/json`. Error: 2'                                
    
    """
    3. Response:
    https://developer.mozilla.org/ru/docs/Web/HTTP/Status
    https://stackoverflow.com/questions/45412228/sending-json-and-status-code-with-a-flask-response
    """
    
    json = request.get_json()
    if not json:
        # 3.1 Simple
        dic = {
            "Example below": True,
            "input1": "1000",
            "input2": "2000",
            "operator": "*"
        }
        return dic,415
        # print(dic['operator'] + dic['input1'] + dic['input2'])
        # responseContent = JSON.dumps(dic)
        
        # # 3.2. Complicated
        # responseContent = JSON.dumps({"input1": 1, "input2": 2, "operator": "/"})
    
        # response = app.response_class(
        #     responseContent,
        #     status=405,
        #     mimetype='application/json'
        # )
        # return response
        
    # General logic
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    json = request.get_json()
    allowed_operators = ['+', '-', '*', '/']
    allowed_json_keys = ['input1', 'input2', 'operator']
    
    # curl -d '{"input2": 1, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # curl -d '{"input1": 1, "operator": "/"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    # curl -d '{"input1": 1, "input2": 1}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/calculator
    for key in allowed_json_keys:
        if key not in json:
            return 'Bad request. Error: 3\n'
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    op1 = json['input1']
    op2 = json['input2']
    operator = json['operator']
        
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    for operand in [op1, op2]:
        if isinstance(operand, int) or isinstance(operand, float):
            continue
        if not is_number(operand):
            return 'Bad request. Error: 4\n'
    
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
        return 'Bad request. Error: 5\n'
    
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
        return 'Bad request. Error: 6\n'