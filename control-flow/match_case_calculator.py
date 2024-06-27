num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if num1 != 0 and num2 != 0:
    match operation:
        case "+":
            print("The result is ",num1+num2)
        case "-":
            print("The result is ",num1-num2)
        case "*":
            print("The result is ",num1*num2)
        case "/":
            print("The result is ",num1/num2)
else:
    print("Cannot divide by zero.")
