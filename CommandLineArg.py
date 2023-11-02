import sys
def addition(num1, num2):
    add = num1 + num2
    return add
def sub(num1, num2):
    s = num2 - num1
    return s
def mul(num1, num2):
    m =num1 * num2
    return m

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation =="add":
    output = addition(num1, num2)
    print(output)
elif operation =="sub":
      output = sub(num1, num2)
      print(output)
elif operation == "mul":
      output = mul(num1, num2)
      print(output)
