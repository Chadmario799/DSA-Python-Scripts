def factorial(y):
    if y == 0 or y == 1:
        return 1
    return y * factorial(y - 1)

x = input("Enter a number: ")
if x[0] == '-':
    print("The Number you have entered is invalid since it is Negative..!")
elif x.__contains__(".") or "." in x:
    print("The Number you have entered is invalid since it has a decimal point..!")
elif not x.isdigit():
    print("The Number you have entered is invalid since it is not a number..!")
else:
    print("The Factorial of", x, "is", factorial(int(x)), "")

