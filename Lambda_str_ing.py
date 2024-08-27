"""
Write a python code using Lambda function to check every element of a List is an Integer or String?
"""

data = [10, '501', 22, 92.2, 'hello', 100, 'world', 87, '351']
result = []

for x in data:
    if isinstance(x, (int, str)):
        result.append(True)
    else:
        result.append(False)

print(result)