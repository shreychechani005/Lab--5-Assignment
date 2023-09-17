N = int(input("Enter the number of lines : "))

if N <= 0:
    print("Please enter a positive integer.")
else:
    i = 1
    
    while i <= N:
        print("* " * i)
        i=i+1