from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI(title="Calculator API")


class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"


class CalculatorRequest(BaseModel):
    number1: float
    number2: float
    operation: Operation


@app.get("/")
def home():
    return {"message": "Welcome to Calculator API. Open /docs to test it."}


@app.post("/calculate")
def calculate(data: CalculatorRequest):
    if data.operation == Operation.add:
        result = data.number1 + data.number2

    elif data.operation == Operation.subtract:
        result = data.number1 - data.number2

    elif data.operation == Operation.multiply:
        result = data.number1 * data.number2

    else:
        if data.number2 == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero."
            )
        result = data.number1 / data.number2

    return {
        "number1": data.number1,
        "number2": data.number2,
        "operation": data.operation,
        "result": result
    }