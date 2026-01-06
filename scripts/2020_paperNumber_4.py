def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

while True:
    number = int(input("Enter a number: "))
    exp = int(input("Enter a power: "))
    if number == -1:
        print("Output: Finished...")
        break
    elif number <= 0 or exp <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        print(f"Output: {power(number, exp)}")