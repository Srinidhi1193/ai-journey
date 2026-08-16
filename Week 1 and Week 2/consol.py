""" Write a function:
def analyze_numbers(nums):
Given:
nums = [12, 7, 25, 4, 18, 31, 10, 9]

Your function should:
Find all even numbers greater than 10.
Find all odd numbers.
Calculate the sum of all numbers.
Find the largest number without using max().
Return all four results."""

def analyze_numbers(nums):
    even = []
    odd = []
    tot = 0
    lar = None
    for num in nums:
        if num % 2 == 0:
            if num > 10:
                even.append(num)
        else:
            odd.append(num)
        tot += num
        if lar is None or num > lar:
            lar = num
    return even,odd,tot,lar

nums = [12, 7, 25, 4, 18, 31, 10, 9]
even, odd, total, largest = analyze_numbers(nums)
print("Even numbers > 10: ",even )
print("Odd numbers: ", odd)
print("Total: ", total)
print("Largest: ", largest)

print()
print("==========Q2===========")
print()

""" 
def analyze_students(students):

The function must:
Calculate each student's average.
Create a dictionary containing:
student → average
Create a list containing students whose average is 80 or above.
Find the student with the highest average.
Return all three results."""

def analyze_students(students):
    stud = {}
    above_avg = []
    gre_avg = None
    gre_name =""
    for name, marks in students.items():
        tot = 0
        for mark in marks:
            tot += mark
        l = len(marks)
        av = tot/l
        avg = round(av,2)
        stud[name] = avg

        if avg >= 80:
            above_avg.append(name)

        if gre_avg is None or avg > gre_avg:
            gre_avg = avg
            gre_name = name
    return stud,above_avg,gre_avg,gre_name

students = {
    "Srinidhi": [85, 90, 92],
    "Rahul": [70, 65, 72],
    "Anu": [95, 88, 91],
    "Karthik": [60, 75, 68]
}
stud,above_avg,gre_avg,gre_name = (analyze_students(students))
print("Averages: ")
print(stud)
print("Above 80: ")
print(above_avg)
print("Highest: ")
print(gre_name, " - ", gre_avg)

print()
print("==========Q3===========")
print()

""" 
def analyze_employees(employees):

Your function must:

1. Create a dictionary of department → employee names

Expected:

{
    "AI": ["Srinidhi", "Anu"],
    "Backend": ["Rahul", "Karthik"]
}
2. Find all employees who know Python

Expected:

["Srinidhi", "Anu"]
3. Find the highest-paid employee in the AI department

Expected:

Anu - 85000
4. Count the total number of employees who know SQL

Expected:

3
5. Return all four results.

So your function should conceptually return:

return department_dict, python_employees, highest_ai_name, sql_count
 """

def analyze_employees(employees):
    depart = {}
    name_lis =[]
    python_emp = []
    hpaid = None
    hiname = ""
    count = 0
    for emp , details in employees.items():
        if details["department"] not in depart:
            depart[details["department"]] = [details["name"]]
        else:
            depart[details["department"]].append(details["name"])
        if "Python" in details["skills"]:
            python_emp.append(details["name"])
        if details["department"] =="AI":
            if hpaid is None or details["salary"] > hpaid:
                hpaid = details["salary"]
                hiname = details["name"]
        if "SQL" in details["skills"]:
            count += 1
    return depart,python_emp,hpaid,hiname,count


employees = {
    "E101": {
        "name": "Srinidhi",
        "department": "AI",
        "skills": ["Python", "ML", "SQL"],
        "salary": 75000
    },
    "E102": {
        "name": "Rahul",
        "department": "Backend",
        "skills": ["Java", "SQL"],
        "salary": 65000
    },
    "E103": {
        "name": "Anu",
        "department": "AI",
        "skills": ["Python", "Deep Learning", "TensorFlow"],
        "salary": 85000
    },
    "E104": {
        "name": "Karthik",
        "department": "Backend",
        "skills": ["Java", "SQL", "Docker"],
        "salary": 70000
    }
}
depart,python_emp,hpaid,hiname,count = analyze_employees(employees)
print("Departments: ")
print(depart)
print("Python employees: ")
print(python_emp)
print("Highest-paid AI:")
print(hiname, " - ", hpaid)
print("SQL employees: ")
print(count)
