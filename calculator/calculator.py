
from art import logo


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations= {"+": add, "-":subtract, "*":multiply, "/":divide }

def calculation():
    print(logo)
    
    num1=float(input("Whats the first number"))

    for symbol in operations:
        print(symbol)
        
    should_continue=True
        
    while should_continue :   
        
        operation_symbol=input("Pick an operation from line above:")
        num2=float(input("Whats the second number"))
        calculation=operations[operation_symbol]
        answer= calculation(num1,num2)
            
        print(f"{num1} {operation_symbol} {num2} = {answer}")    
        
        if input(f"Type 'y' to continue calculating with {answer}") == "y":
            num1= answer
        else:
            should_continue=False
            calculation()

calculation()

# if operation_symbol == "+":
#     answer= add(num1,num2)
# elif operation_symbol =="-" :
#     answer = subtract(num1,num2)
# elif operation_symbol == "*":
#     answer= multiply(num1,num2)
# elif operation_symbol== "/":
#     answer= divide(num1,num2)     
    #**********OR*************
    