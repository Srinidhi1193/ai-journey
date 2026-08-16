print("hello")
name = "Sri"
age = 20
price = 22.50
status = False
print("name: ",name,end="\n" )
print("age: ",age,end="\n" )
print("price: ",price,end="\n" )
print("status: ",status,end="\n" )
print(type(status))

""" Logical operator """
""" bool of any non-empty string is true """
pre_age = int(input("Enter your present age"))
has_id = input("Do you have ID? (yes/no): ").strip().lower() == "yes"
if(pre_age>=18 and has_id == True):
    print("Eligible")
else:
    print("Not Eligible")
""" Combined operators """
marks= int(input("Enter your mark"))
if((marks >= 50) and (marks <= 100)):
    print("True")
else:
    print("False")
""" Assignment Operators """
score = 10
score += 10
print(score)   
score -= 10
print(score)   
score *= 10
print(score)   
score /= 10
print(score)