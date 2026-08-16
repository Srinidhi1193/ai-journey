""" Asks the user to enter a password (a string)
Using a loop, go through the password character by character and count:
How many digits it contains (0-9)
How many uppercase letters it contains
How many lowercase letters it contains
How many special characters it contains (anything that's not a letter or digit — e.g. @ # $ % ! * etc.)
After the loop, decide the password's strength using these rules:
Strong: length >= 8 and has at least 1 digit and at least 1 uppercase and at least 1 special character
Medium: length >= 6 but doesn't meet all the Strong conditions
Weak: anything else (length < 6)
Print all four counts, then print the final strength. """
digit =0
upper =0
lower =0
spl =0
password = str(input("Enter your password: "))
for char in password:
    if char.isnumeric():
        digit+=1
    elif char.isupper():
        upper+=1
    elif char.islower():
            lower+=1
    else:
         spl+=1
print("digit", digit)
print("Uppercase", upper)
print("Lowercase", lower)
print("special", spl)    
if(len(password)>=8) and digit>=1 and upper>=1 and spl>=1:
     print("Strong")
elif(len(password)>=6):
     print("Medium")
else:
     print("Weak")
     

    
