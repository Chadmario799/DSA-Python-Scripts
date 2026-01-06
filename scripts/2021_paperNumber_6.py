def series(num):
    if num == 1:
        return 1
    return series(num-1) + 2**(num-1)

while True:
    number = int(input("Enter a number: "))
    if number == -1:
        print("Output: Output: Finished...")
        break
    elif number <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        print(f"Output: {series(number)}")