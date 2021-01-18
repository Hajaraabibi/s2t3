print("Hello there! Welcome to simple calculator coded with python!")
selectoperator = input(''' * multiply     + add      - subtract    / divide
Choose from the list of maths operators above what sum you would like to carry out: 
''')

numberOne = int(input("type in your first number: "))
numberTwo = int(input("type in your second number: "))

if selectoperator == "*":
    print("The answer to your multiplication sum is:")
    print(numberOne * numberTwo)

    print("Thank you for using this calculator!")
elif selectoperator == "+":
    print("The answer to your addition sum is: ")
    print(numberOne + numberTwo)

    print("Thank you for using this calculator!")
elif selectoperator == "-":
    print("The answer to your subtraction sum is: ")
    print(numberOne - numberTwo)

    print("Thank you for using this calculator!")
elif selectoperator == "/":
    print("The answer to your division sum is: ")
    print(numberOne / numberTwo)

    print("Thank you for using this calculator!")
else:
    print("The operator you entered is not valid please try again.")
