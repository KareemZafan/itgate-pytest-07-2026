import math 

def add(a, b):
    return a + b

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division By Zero")
    return a / b

def power(a, b):
    return math.pow(a, b)

def sqrt(a):
    if a < 0:
        raise ValueError("Input must be a non-negative number")
    return math.sqrt(a)

def abs(a):
    if a < 0:
        return -a
    return a

def mod(a, b):
    if b == 0:
        raise ValueError("Division By Zero")
    return a % b

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

