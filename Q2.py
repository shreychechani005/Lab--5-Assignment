
N = int(input("Enter a positive integer N: "))

if N <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Numbers not divisible by {N} in the range 1 to 1000:")
    
    number = 1

    while number <= 1000:

        if number % N ==0:
            number += 1
            continue
        
        print(number, end=' ')
        
        number += 1

    print()  
