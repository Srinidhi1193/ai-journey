a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if(a>b and a>c):
    print("Largest is ",a)
elif(b>c and b>a):
    print("Largest is ",b)
else:
    print("Largest is ",c)
