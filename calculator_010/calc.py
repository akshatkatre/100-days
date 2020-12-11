from calculator_010.art import logo
print(logo)



# Calculator

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}

def calculator():
  continue_calculation = True
  num1 : int= None
  num2 : int = None

  while continue_calculation:
    if num1 is None:
      num1 = float(input('Enter first number : '))
    for operation in operations:
      print(operation)
    operation = input('Enter operation : ')
    num2 = float(input('Enter second number : '))
    function = operations[operation]
    result = function(num1, num2)
    print(f'{num1} {operation} {num2} = {result}')
    user_response = input(f"Type 'y' to continue with {result}, to type 'n' to stop:")
    if user_response == 'y':
      num1 = result
    else:
      continue_calculation = False
      calculator()

calculator()