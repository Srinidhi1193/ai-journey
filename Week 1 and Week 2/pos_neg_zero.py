num = int(input("Give a number: "))
if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print ("zero")

age = int(input("Give a number: "))
if(age>13):
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
