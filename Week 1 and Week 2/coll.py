""" Write a program that:

Iterates through the students list.
Finds all students whose CGPA is 8.5 or above.
Creates a dictionary where:
key → student name
value → CGPA
Prints the resulting dictionary.
Finds and prints the student with the highest CGPA."""

students = [
    ("Srinidhi", "AI", 8.91),
    ("Rahul", "Backend", 7.85),
    ("Anu", "AI", 9.20),
    ("Karthik", "Data Science", 8.40)
]

result = {}
h_cgpa = 0
h_name = ""
print("Students with CGPA >= 8.5: ")
for student in students:
    if student[2] >= 8.5:
        result[student[0]] = student[2]
    if student[2] > h_cgpa:
        h_cgpa = student[2]
        h_name = student[0]
print(result)
print("Highest CGPA:")
print(h_name, " - ",h_cgpa)

""" 
Calculates the average mark for every student.
Creates a new dictionary:
{
    "Srinidhi": 89.0,
    "Rahul": 71.0,
    ...
}
Creates a tuple containing the names of students whose average is 80 or above.
Finds the student with the highest average.
Don't use sum() or max().
Expected important results
Average dictionary:
Srinidhi → 89.0
Rahul → 71.0
Anu → 91.33
Karthik → 80.0

Students with average >= 80:
("Srinidhi", "Anu", "Karthik")

Highest average:
Anu - 91.33 """

students = {
    "Srinidhi": ("AI", [85, 90, 92]),
    "Rahul": ("Backend", [70, 75, 68]),
    "Anu": ("AI", [95, 88, 91]),
    "Karthik": ("Data Science", [80, 82, 78])
}

print("=====q2=====")
print()
stud = {}
tup_st = ()
hag = 0
qual =[]
hname =""
print("Average dictionary: ")
for key, value in students.items():
    tot = 0
    for num in value[1]:
        tot += num
    l = len(value[1])
    avrg = tot/l
    stud[key] = avrg
    if avrg >= 80:
        qual.append(key)
    tup_st = tuple(qual)
    if avrg > hag:
        hag = avrg
        hname = key

print(stud)
print("Students with average >= 80: ")
print(tup_st)
print("Highest average: ")
print(hname, " - ",hag)

print()
print("=========Q3=========")
print()

""" Q4 — Final Challenge: Collections Mini-Program

You are given a list of tuples containing employee sales:

Each tuple contains:

(name, department, sales_amount)

Write a program that:

1. Create a dictionary containing total sales by department

Expected:

{
    "AI": 155000,
    "Backend": 80000
}
2. Create a tuple containing employees whose sales are above 40,000

Expected:

("Srinidhi", "Anu", "Karthik")
3. Find the employee with the highest sales

Expected:

Highest sales: Anu - 65000 """


sales = [
    ("Srinidhi", "AI", 50000),
    ("Rahul", "Backend", 35000),
    ("Anu", "AI", 65000),
    ("Karthik", "Backend", 45000),
    ("Meena", "AI", 40000)
]

dep_sale ={}
tot = 0
h_tup =()
h_lis = []
h_sale = 0
h_name = ""
for sale in sales:
    if sale[1] not in dep_sale:
        dep_sale[sale[1]] = sale[2]
    else:
        dep_sale[sale[1]] += sale[2]
    if sale[2] > 40000:
        h_lis.append(sale[0])

    if sale[2] > h_sale:
        h_sale =sale[2]
        h_name = sale[0]

print(dep_sale)
h_tup = tuple(h_lis)
print("Employees whose sales are above 40,000: ")
print(h_tup)
print("Highest sales: ",h_name, " - " ,h_sale)
