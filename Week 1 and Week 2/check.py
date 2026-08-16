""" R3 — Final Mixed Revision Challenge 🔥

You are given purchase data:
Each tuple contains:

(order_id, customer, category, price, quantity)

Write a function:

def analyze_orders(orders):
Your function must:

1. Calculate each order's total value

price × quantity

Create a dictionary:

{
    "O101": 150000,
    "O102": 36000,
    ...
}

2. Calculate total spending by customer

Expected:

{
    "Srinidhi": 166000,
    "Rahul": 36000,
    "Anu": 19500
}

3. Create a tuple of customers whose total spending is above ₹50,000

Expected:

("Srinidhi",)

4. Find the highest-value order

Expected:

O101 - 150000

5. Return all four results. """

def analyze_orders(orders):
    tot = 0
    ord_id = {}
    ord_cus = {}
    spen_lis = []
    spen_tup = ()
    hi_val = None
    hi_id = ""
    for ord in orders:
        tot = ord[3]*ord[4]
        ord_id[ord[0]] = tot

        if ord[1] not in ord_cus:
            ord_cus[ord[1]] = tot
        else:
            ord_cus[ord[1]]+=tot

        if hi_val is None or tot > hi_val:
            hi_val = tot
            hi_id = ord[0]
            
    for customer, spending in ord_cus.items():
                if spending > 50000:
                    spen_lis.append(customer)
    spen_tup = tuple(spen_lis)
    return ord_id,ord_cus,spen_tup,hi_id,hi_val

orders = [
    ("O101", "Srinidhi", "Electronics", 75000, 2),
    ("O102", "Rahul", "Furniture", 12000, 3),
    ("O103", "Anu", "Electronics", 1500, 5),
    ("O104", "Srinidhi", "Furniture", 8000, 2),
    ("O105", "Anu", "Electronics", 3000, 4)
]

ord_id,ord_cus,spen_tup,hi_id,hi_val = analyze_orders(orders)
print(ord_id)
print(ord_cus)
print(spen_tup)
print(hi_id ," - ", hi_val)