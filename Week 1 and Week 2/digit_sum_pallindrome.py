""" Asks the user to enter a number n
Using a loop (no string conversion — do it purely with math: % and //), calculate:
The sum of its digits
The reversed number
After the loop, check if the number is a palindrome (reads the same forwards and backwards — meaning n equals its reversed version)
Print the digit sum, the reversed number, and whether it's a palindrome or not """

num = abs(int(input("Enter a number: ")))
ori = num
tot =0
rev = 0
while num>0:
    dig = num % 10
    tot += dig
    rev = rev*10 + dig
    num = num//10
print("Sum of digits: ",tot)
print("Reverse: ", rev)
if(ori == rev):
    print("Pallindrome")
else:
    print("Not a Pallindrome")


