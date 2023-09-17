num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 <= 0 or num2 <= 0:
    print("Invalid input")
else:
    if num1 > num2:
        max_num, min_num = num1, num2
    else:
        max_num, min_num = num2, num1

    lcm = max_num

    while lcm % min_num != 0:
        lcm += max_num

    print(f"The LCM of {num1} and {num2} is {lcm}")