"""
Using python Lamda function create a Fibonacci series from 1 to 50 elements?
"""

def fibonacci(n):
    result = [0, 1]  
    for i in range(2, n):
        next_value = result[-1] + result[-2]  
        result.append(next_value)  
    return result

result = fibonacci(50)
print("List of Fibonacci series up 1 to 50 : ", result)