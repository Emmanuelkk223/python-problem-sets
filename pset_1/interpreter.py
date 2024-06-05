expression = input("Expression: ")
a, op, b = expression.split()

a = int(a)
b = int(b)
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)


