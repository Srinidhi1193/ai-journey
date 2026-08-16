""" String Loop """

text = input("Enter a string: ")
for char in text:
    print(char)

""" For Loop """
numbers = [10, 20, 30, 40, 50]
tot =0
for i in numbers:
    tot = tot+i
print(tot)

""" While Loop """
num =5
while num>=1:
    print (num)
    num = num -1
print("Go!")

choice = 0

while choice != 3:
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Hello!")
    elif choice == 2:
        print("Goodbye!")
    elif choice == 3:
        print("Exiting...")
    else:
        print("Invalid choice")