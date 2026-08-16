import math

num = int(input("Enter a number: "))
for i in range (num):
    for j in range(i+1):
        print(j+1, end =" ")
    print()

pos = abs(num)
if(pos == 0 or pos ==1):
    print("Not a prime")
    
for i in range(int(math.sqrt(pos))):
    if num % i == 0:
        print("Prime number")
        break;
    else:
        print("Not a prime number")
