""" Asks the user to enter numbers one at a time, using a loop that runs 10 times
As you go, keep track of:
How many numbers were even
How many numbers were odd
The sum of all numbers entered
The largest number entered so far
After the loop ends, print all four results: """
even  =0
odd = 0
tot =0
largest = None
for i in range(10):
    num = int(input("enter your num"))
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    tot = tot + num
    if largest is None or num > largest:
        largest = num
print("How many numbers were even: ", even)
print("How many numbers were odd: ", odd)
print("The sum of all numbers entered", tot)
print("The largest number entered so far", largest)

    