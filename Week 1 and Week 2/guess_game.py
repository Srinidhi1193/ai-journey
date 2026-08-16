secret = 7
num = int(input("Please enter a number"))
while num != secret:
    if(num > secret):
        print("Too High")
    elif(num < secret):
        print("Too less")
    num = int(input("Guess again: "))
print("Correct!")
