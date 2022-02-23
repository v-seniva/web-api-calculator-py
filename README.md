 <h1>WEB-API-CALCULATOR-PY</h1>


# web-api-calculator-py


This small web api calculator is written in Python, created with Flask and deployed to Heroku.

Please use following curl commands to performs required actions:

To add up 2 numbers -

curl -d '{"input1": 1, "input2": 2, "operator": "+"}' -H "Content-Type: application/json" -X POST  https://web-api-calculator-py.herokuapp.com/calculator ;

To substract one number from another -

curl -d '{"input1": 1, "input2": 2, "operator": "-"}' -H "Content-Type: application/json" -X POST https://web-api-calculator-py.herokuapp.com/calculator ;

To divide one number with another -

curl -d '{"input1": 1, "input2": 2, "operator": "/"}' -H "Content-Type: application/json" -X POST https://web-api-calculator-py.herokuapp.com/calculator ;

To multiply 2 numbers -

curl -d '{"input1": 1000000, "input2": 1000000, "operator": "*"}' -H "Content-Type: application/json" -X POST https://web-api-calculator-py.herokuapp.com/calculator .


