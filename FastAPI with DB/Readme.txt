# Expense Tracker API

A RESTful Expense Tracker API built using Python, FastAPI, SQLAlchemy, and MySQL. The API supports CRUD operations for managing expenses along with additional endpoints for expense analysis.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- MySQL
- MySQL Connector/Python
- Swagger UI

## Project Structure

```text
FastAPI with DB/
│
├── Main.py
├── database.py
├── expense.py
├── expense_db.py

1. Add Expense

POST /expense

Adds a new expense to the database.

Request:
{
  "id": 7,
  "category": "Snacks",
  "amount": 900
}

Response:
"Expense added successfully"

2. Get All Expenses

GET /expenses
Returns all expenses stored in the database.

Response:
[
  {
    "id": 1,
    "category": "Food",
    "amount": 500
  },
  {
    "id": 2,
    "category": "Food",
    "amount": 300
  },
  {
    "id": 3,
    "category": "Skincare",
    "amount": 900
  },
  {
    "id": 4,
    "category": "Electronics",
    "amount": 1200
  },
  {
    "id": 5,
    "category": "Groceries",
    "amount": 1000
  }
]

3. Get Expenses by Category

GET /expenses/{cat}
Returns all expenses belonging to a specific category.

Example Request:
GET /expenses/Food

Response:
[
  {
    "id": 1,
    "category": "Food",
    "amount": 500
  },
  {
    "id": 2,
    "category": "Food",
    "amount": 300
  }
]

If the category does not exist:
{
  "message": "No such category"
}

4. Get Total Expenses
GET /totexp
Calculates the total amount of all expenses stored in the database.

Response:
{
  "total": 4800.0
}
The returned value depends on the current data in the database.

5. Get Highest Expense
GET /highexp
Returns the highest expense amount stored in the database.

Response:
{
  "Highest expense": 1200.0
}

6. Update Expense
PUT /expense/{id}
Updates the category and amount of an existing expense using its ID.

Example Request:
PUT /expense/7

Request Body:
{
  "id": 7,
  "category": "Restaurant",
  "amount": 1200
}

Response:
"Expense updated"

If the ID does not exist:
"Expense with this id does not exist"

7. Delete Expense
DELETE /expense/{id}
Deletes an expense from the database using its ID.

Example Request:
DELETE /expense/7

Response:
"Expense deleted"

If the ID does not exist:
"Expense with this id does not exist"