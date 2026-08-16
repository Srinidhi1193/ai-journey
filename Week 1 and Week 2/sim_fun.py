""" Simple function """

def greet():
    print("Hello, welcome to Python!")

greet()

""" function wih parameter """

def greetname(name):
    print("Hello,",name+"!")

greetname("Srinidhi")

""" Function with Return """

def add(a,b):
    sum = a+b
    print(sum)

add(3,4)

""" Create a function:

calculator(a, b, operator) """

def calculator(a, b, oper):
    if oper == '+':
        ans = a+b
    elif oper == '-':
        ans = a-b
    elif oper == '*':
        ans = a*b
    elif oper == '/':
        ans = a/b
    else:
        return "invalid operator"

    return ans

print(calculator(4,9,"-"))

""" square(num) """

def square(num):
    return num*num

n = int(input("Enter a number: "))
print(square(n))

""" Largest of three numbers """

def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:
        return c

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
print("largest number is" ,largest(a,b,c)) 

"""factorial"""

def factorial(num):
    fact = 1
    for i in range(num,1,-1):
        fact = fact * i
    return fact
print(factorial(3))

""" Accept one parameter.
Return:
"Prime" if the number is prime.
"Not Prime" otherwise.
Do not use any built-in functions.
Use a for loop.
Take input from the user.
Print the returned value. """

def isprime(num):
    if num < 2:
        return "Not prime"
    for i in range(2,num):
        if num % i ==0:
            return "Not prime"
            break;
    return "Prime"
num = int(input("Enter a number: "))
print(isprime(num))

        
""" Accept a string.
Count how many vowels (a, e, i, o, u) are present.
Return the count.
Take input from the user.
Print the returned value.
 """

def vow_count(user):
    count = 0
    word = user.lower()
    for char in word:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
            count +=1
    return count

userr = input("Enter a word: ")
print(vow_count(userr))

""" Accept a string.
Return the reversed string.
Take input from the user.
Print the returned result.
Do not use reversed()."""

def rev_word(word):
    rev = ""
    l = len(word)
    for i in range(l-1,-1,-1):
        rev += word[i]
    return rev
user = input("Enter a word: ")
print(rev_word(user))


