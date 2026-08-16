""" Asks the user to enter marks for 5 subjects (use a loop to collect them)
Keeps a running total as you go
After the loop, calculates the average
Based on the average, prints a grade using this scale:
>= 90 → "A"
>= 75 → "B"
>= 50 → "C"
below 50 → "Fail" """
total = 0
for i in range(5):
    mark = int(input("enter your mark"))
    total = total + mark
avg = total/5
if(avg>=90):
    print("Grade is A")
elif(avg>=75):
    print("Grade is B")
elif(avg>=50):
    print("Grade is C")
else:
    print("Fail")
