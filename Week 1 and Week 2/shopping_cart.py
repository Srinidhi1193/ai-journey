""" Write a program that:

Asks the user how many items they want to buy (call this n)
Using a loop that runs n times, for each item ask for:
The item's price
The quantity being bought
Keep a running grand total (price × quantity for each item, added up across all items)
While looping, also track:
The most expensive single item (by price, not price×quantity)
How many items were bought in bulk (quantity >= 5)
After the loop:
If grand total > 2000, apply a 10% discount to the final total
Print: grand total (after discount if applicable), the most expensive item's price, how many items were bulk purchases, and whether a discount was applied """

n = int(input("Enter the items that you want: "))
tot = 0
bulk = 0
price = 0
dis = False
for i in range(n):
    item = float(input("Enter the items price: "))
    quan = float(input("Enter the no of items that you want: "))
    tot = item*quan + tot
    if item > price:
        price = item
    if quan>=5:
        bulk += 1
if(tot > 2000):
    tot -= (tot*10)/100
    dis = True
print("The most expensive single item by price: ",price)
print("No of items bought in bulk: ",bulk)
print("Grand total: ", tot)
if dis == True:
    print("Discount applied")
else:
    print("No discount")



