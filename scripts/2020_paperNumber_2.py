def fibonacci(n):
    if n <= 0:
        return n
    else:
        return abs(fibonacci(n-1) + fibonacci(n-2))

while True:
    number = int(input("Enter a number: "))
    if number == -1:
        print("Output: Finished...")
        break
    else:
        print(f"Output: {fibonacci(number)}")