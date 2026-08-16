""" Create a tuple containing 5 values of your choice.

Your program should:

Print the complete tuple.
Print the first element.
Print the last element using negative indexing.
Print the third element.

Use indexing only for accessing the elements. """

tup = (1,2,3,4,5)
print(tup)
print(tup[0])
print(tup[-1])
print(tup[2])


""" Write a program to:

Find the length of the tuple.
Count how many times 20 appears.
Find the index of the first occurrence of 40.
Check whether 50 exists in the tuple.

Use appropriate tuple operations/methods. """

tup = (10,20,30,20,40,60)
print(len(tup))
print(tup.count(20))
print(tup.index(40))
print(50 in tup)

""" Given:

tup = (10, 20, 30, 40)
Try to:
Change 20 to 25.
Add 50 to the tuple.
Remove 30 from the tuple. """

tup = (10, 20, 30, 40)
lst = list(tup)
lst[1] = 25
lst.append(50)
lst.remove(30)

tupl = tuple(lst)
print(tupl)

""" Create a function:
student_details(student)
Given:
student = ("Srinidhi", 20, "AI", 8.9)
The function should:
Extract the name, age, course, and CGPA from the tuple.
Return the name and CGPA.
Print the returned result.
 """
def student_details(student):
    name = student[0]
    cgpa = student[3]
    return (name,cgpa)
student = ("Srinidhi", 20, "AI", 8.9)
name, cgpa = student_details(student)

print("Name:", name)
print("CGPA:", cgpa)
