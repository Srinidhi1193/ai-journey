""" 1. Create a project folder named student-report-card.
2. Write down the required inputs: Student ID, name and subject marks.
3. Decide the subjects you will support, for example Maths, English and Science.
4. Create input statements for Student ID and student name.
5. Create a dictionary to store subject names and marks.
6. Add input validation so marks are sensible numbers.
7. Create a function to calculate total marks.
8. Create a function to calculate the average.
9. Create grade rules using if/elif/else.
10. Create a function that returns the grade.
11. Print Student ID, name, each subject mark, total, average and grade neatly.
12. Test with a high-scoring student.
13. Test with average and low-scoring students, including boundary marks.
14. Refactor repeated logic into functions and add simple error handling.
15. Save final code and a sample output screenshot/readme for your portfolio. """

def get_student_details():
    stud_det = {}
    sub_marks ={}
    stud_list = ["ID","Name"]
    marks = ["english","math","science"]
    for det in stud_list:
        detail = input("Please enter your " + det + ": ")
        stud_det[det] = detail

    for mar in marks:
        while True:
            try:
                mark = int(input(f"Please enter your {mar} mark for 100: "))
                if mark < 0 or mark > 100:
                    print("Please enter a mark between 0 and 100.")
                    continue
                sub_marks[mar] = mark
                break
            except ValueError:
                print("Non-numeric value entered for marks")
    return stud_det,sub_marks

def total_marks(sub_mark_store):
    tot = 0
    for mark in sub_mark_store.values():
        tot += mark
    return tot

def average_marks(sub_mark_store):
    no_of_sub = len(sub_mark_store)
    mark_obt = total_marks(sub_mark_store)
    avg = round(mark_obt/no_of_sub, 2)

    return avg

def grade(sub_mark_store):
    tot_grade = average_marks(sub_mark_store)
    if tot_grade >=80 :
         return "A"
    elif tot_grade >= 60:
         return "B"
    elif tot_grade >= 40:
         return "C"
    else:
         return "Fail"       

stud_det,sub_marks = get_student_details()
tot = total_marks(sub_marks)
avg = average_marks(sub_marks)
grad = grade(sub_marks)

print("======================================")
print("          STUDENT REPORT CARD         ")
print("======================================")
print()
print("Student details")
print("ID: ",stud_det["ID"])
print("Name: ",stud_det["Name"])
print()
print("Marks")
print("English: ",sub_marks["english"])
print("Maths: ",sub_marks["math"])
print("Science: ",sub_marks["science"])
print()
print("Total marks: ",tot)
print("Average: ",avg)
print("Grade: ",grad)
print("==============THANK YOU===============")

