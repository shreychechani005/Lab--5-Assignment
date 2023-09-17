n = int(input("Please Enter the Total Number of Rows: "))
i = 1

while i <= n:
    spaces = ' ' * (n - i)
    stars = '*' * i
    pattern = spaces + stars
    print("The pattern is as follows: \n")
    print(pattern)
    i = i + 1
