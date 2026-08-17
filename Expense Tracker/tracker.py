""" 1. Create a project folder named personal-expense-tracker.
2. Define each expense as category + amount.
3. Create an empty list that will hold expense dictionaries.
4. Create an Add Expense function.
5. Take category and amount from the user.
6. Validate that the amount is numeric and positive.
7. Append each expense dictionary to the list.
8. Create a function to display all expenses.
9. Create a function to calculate total spent.
10. Create a function to find the highest expense.
11. Create a function to filter/display expenses by category.
12. Create a simple menu so the user can choose operations.
13. Test with Food, Travel and Shopping examples.
14. Handle empty-list and unknown-category cases.
15. Clean the code; this becomes the base for the later FastAPI project """


def add_expense():
    while True:
        category = input("Enter category: ")
        if not category.strip():
            print("Category cannot be empty")
            continue
        break
    while True:
        try:
            amt = float(input("Enter amount: "))
            if amt <= 0:
                print("Enter a valid amount")
            else:
                break
        except ValueError:
                    print("Amount cannot have non-numeric values")
    expen_dic = {}
    expen_dic[category] = amt
    expen_lis.append(expen_dic)
    return expen_lis

def display_expenses():
    if len(expen_lis) == 0:
        show = "No items to display"
    else:
        show = expen_lis
    return show

def total_expense(expen_lis):
    tot = 0
    for pair in expen_lis:
        for expen in pair.values():
            tot += expen
    return tot

def highest_expense(expen_lis):
    hi_expen = None
    hi_cat = "Items not yet added"
    for pair in expen_lis:
        for cat, expen in pair.items():
            if hi_expen is None or expen > hi_expen:
                hi_expen = expen
                hi_cat = cat
    return hi_expen,hi_cat

def filter_expense(expen_lis, category):
    fil_list = []
    for expen in expen_lis:
        for cat, exp in expen.items():
            if cat == category:
                fil_dict = {}
                fil_dict[cat] = exp
                fil_list.append(fil_dict)
    if len(fil_list) == 0:
        return "No items found in the given category"
    return fil_list

expen_lis = []
print("===========================")
print("============MENU===========")
print("===========================")
while True:
    try:
        num = int(input("Enter your choice: "))
    except ValueError:
        print("Choice cannot have non-numeric values")
        continue
    match num:
        case 1:
            expen_lis = add_expense()
            print("Expense added")
        case 2:
            print("Displaying expense.... ")
            show = display_expenses()
            print(show)
        case 3:
            tot = total_expense(expen_lis)
            print("Total expense: ",tot)
        case 4:
            hi_expen,hi_cat = highest_expense(expen_lis)
            print("Highest expense: ", hi_cat, " - ", hi_expen)
        case 5:
            category = input("Enter category to filter: ")
            fil_list = filter_expense(expen_lis, category)
            print("Expense in", category ," : " ,fil_list)
        case 6:
            print("Exiting...THANK YOU")
            break
        case _:
            print("Invalid choice")
            
     

    







