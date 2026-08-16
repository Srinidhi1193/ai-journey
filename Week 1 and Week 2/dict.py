""" Write a program that:

Prints the student's name and cgpa.
Updates the cgpa to 8.9.
Adds a new key "city" with value "Chennai".
Prints the updated dictionary.

Don't use loops or functions yet. """

student = {
    "name": "Srinidhi",
    "age": 20,
    "course": "AI",
    "cgpa": 8.5
}
print(student.get("name","NA"))
print(student.get("cgpa","NA"))
student["cgpa"]= 8.91
student["city"] = "chennai"
print(student)

""" Create a program that:

Iterates through both keys and values.
Prints every subject and mark.
Finds and prints the highest mark and its subject.
Prints the subjects where the mark is 80 or above.
Do not use max(). """

marks = {
    "Maths": 85,
    "Python": 92,
    "SQL": 78,
    "Machine Learning": 95,
    "Statistics": 68
}
maxi =0
max_subject = ""
for key, value in marks.items():
    print(key ," : ", value)
    if value >= 80:
        print("80 above: ",key ," - ", value)
    if value > maxi:
        maxi = value
        max_subject = key
print("highest - ", maxi ," - ", max_subject)

""" Write a program that:

Iterates through the dictionary.
Calculates each student's average.
Do not use sum().
Print each student's name and average.
Print only students whose average is 80 or above.
Find the student with the highest average. """

students = {
    "Srinidhi": [85, 90, 78],
    "Rahul": [70, 65, 72],
    "Anu": [92, 88, 95],
    "Karthik": [60, 75, 68]
}
maxmum = 0
max_sub = ""
for key, value in students.items():
    tot = 0
    for num in value:
        l = len(value)
        tot += num
    avg = tot/l
    print("Average ", key ," - ", avg)
    if (avg>=80):
        print("first class :", key)
    if(avg>maxmum):
        maxmum = avg
        max_sub = key
print("highest",max_sub, " = ",maxmum)
    
""" Write a program that:

Iterates through all employees.
Prints each employee's:
ID
Name
Department
Salary
Prints only employees from the "AI" department.
Finds the employee with the highest salary.
Do not use max(). """

employees = {
    "E101": {
        "name": "Srinidhi",
        "department": "AI",
        "salary": 75000
    },
    "E102": {
        "name": "Rahul",
        "department": "Backend",
        "salary": 65000
    },
    "E103": {
        "name": "Anu",
        "department": "AI",
        "salary": 85000
    }
}

print("EMPLOYEE DETAILS")
max_sal = 0
max_emp = ""
for key, value in employees.items():
    print("ID : ", key)
    print("Name : ",value["name"])
    print("Department : ",value["department"])
    print("Salary : ",value["salary"])

    if(value["department"] == "AI"):
        print("AI folks: ", value["name"])

    if value["salary"] > max_sal:
        max_sal = value["salary"]
        max_emp = value["name"]
print("highest -- ",max_sal ,"-" , max_emp)

""" Write a program that:

Prints each employee's name and all their skills.
Finds and prints employees who know Python.
Finds and prints employees who belong to the AI department AND know Python.
Counts the total number of employees who know Python. """

employees = {
    "E101": {
        "name": "Srinidhi",
        "department": "AI",
        "skills": ["Python", "ML", "SQL"]
    },
    "E102": {
        "name": "Rahul",
        "department": "Backend",
        "skills": ["Java", "Spring", "SQL"]
    },
    "E103": {
        "name": "Anu",
        "department": "AI",
        "skills": ["Python", "Deep Learning", "TensorFlow"]
    }
}

print()
print()
count=0
for keyy, valuee in employees.items():
    print("Name: ", valuee["name"], " -> ", "Skills: ",valuee["skills"])
    if "Python" in valuee["skills"] :
        print("Employees who know python:")
        print(valuee["name"])
        count +=1
    if valuee["department"] == "AI" and "Python" in valuee["skills"] :
        print("Employees who know python and are in AI department:")
        print(valuee["name"])
print("No of emp who know python: ", count)




orders = {
    "order1": {
        "product": "Laptop",
        "category": "Electronics",
        "price": 75000
    },
    "order2": {
        "product": "Mouse",
        "category": "Electronics",
        "price": 1500
    },
    "order3": {
        "product": "Chair",
        "category": "Furniture",
        "price": 8000
    },
    "order4": {
        "product": "Keyboard",
        "category": "Electronics",
        "price": 3000
    },
    "order5": {
        "product": "Desk",
        "category": "Furniture",
        "price": 12000
    }
}
print()
print("***********")
tot = 0
ele_tot = 0
e_count = 0
f_count = 0
fur_tot = 0
pri_max = 0
prod_max = ""
for key, value in orders.items():
    tot += value["price"]
    
    if value["category"] == "Electronics":
        ele_tot += value["price"]
        e_count +=1
    if value["category"] == "Furniture":
        fur_tot += value["price"]    
        f_count +=1
    if value["price"] >  pri_max:
        pri_max = value["price"]
        prod_max = value["product"]
print("Total order value: ",tot)
print ("Electronics value: ", ele_tot)
print("Furniture value: ", fur_tot)
print("Electronics orders:", e_count)
print("Furniture orders:", f_count)
print ("Most expensive: ",prod_max, " - ",pri_max)

"""real problem
Your program must:
Print the names of all AI employees.
Print the names of employees who know Python.
Find the highest-paid AI employee.
Calculate the average salary of all employees.
❌ Don't use sum().
Count how many employees know SQL.
Print the final results clearly."""

print("================")
emp = {
    "E101": {
        "name": "Srinidhi",
        "department": "AI",
        "skills": ["Python", "SQL", "ML"],
        "salary": 75000
    },
    "E102": {
        "name": "Rahul",
        "department": "Backend",
        "skills": ["Java", "Spring", "SQL"],
        "salary": 65000
    },
    "E103": {
        "name": "Anu",
        "department": "AI",
        "skills": ["Python", "ML", "TensorFlow"],
        "salary": 85000
    },
    "E104": {
        "name": "Karthik",
        "department": "Backend",
        "skills": ["Java", "SQL", "Docker"],
        "salary": 70000
    }
}
total_salary = 0
highest_ai_salary = 0
highest_ai_employee = ""
sql_count = 0

ai_employees = []
python_employees = []

for key, value in emp.items():

    total_salary += value["salary"]

    if value["department"] == "AI":
        ai_employees.append(value["name"])

        if value["salary"] > highest_ai_salary:
            highest_ai_salary = value["salary"]
            highest_ai_employee = value["name"]

    if "Python" in value["skills"]:
        python_employees.append(value["name"])

    if "SQL" in value["skills"]:
        sql_count += 1

average_salary = total_salary / len(employees)

print("AI Employees:")
for name in ai_employees:
    print(name)

print("\nPython Employees:")
for name in python_employees:
    print(name)

print("\nHighest-paid AI employee:")
print(highest_ai_employee, "-", highest_ai_salary)

print("\nAverage salary:")
print(average_salary)

print("\nEmployees knowing SQL:")
print(sql_count)
    

