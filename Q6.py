num1 = int(input(" Enter number 1 : "))
num2= int(input(" Enter number 2 : "))
if num1<=0 or num2<=0:
    print("Invalid input ")

i = 1
while(i <=num1 and i <=num2):
    if(num1 % i == 0 and num2 % i == 0):
        gcd = i
    i = i + 1  
print(f'The HCF/GCD of {a} and {b} is {gcd}')