def cubic_series_test(num):
    if num == 1:
        return 3
    elif num == 2:
        return 14
    else:
        return 2 * cubic_series_test(num - 1) - cubic_series_test(num - 2) + 6 * num - 4

while True:
    uinput = int(input("Enter Number : "))
    if uinput == -1:
        print("Output : Finished..")
    elif uinput <= 0:
        print("Invalid Input. Please Enter a Positive Integer")
    else:
        print("Output : ", cubic_series_test(uinput))