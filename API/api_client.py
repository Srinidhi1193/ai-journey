import requests
import json

""" Get request """

def get_user():
    url_get = "https://jsonplaceholder.typicode.com/users"
    response_get = requests.get(url_get)
    f_res = response_get.json()
    print("====DETAILS OF ALL ID=====")
    for num in f_res:
        print("User ID:", num["id"])
        print("User name:", num["username"])
        print("Email:", num["email"])
        print("City:", num["address"]["city"])
        print("Street:", num["address"]["street"])
    with open("api_client_res.json", "w") as af:
        json.dump(f_res, af, indent=2)
    print("Response saved")

""" Get one request """

def get_one_user():
    user_id = int(input("Enter a user ID: "))
    url_get_one = f"https://jsonplaceholder.typicode.com/users/{user_id}"  
    response_get_one = requests.get(url_get_one)
    print(response_get_one)
    if response_get_one.status_code == 200:
        f_res_one = response_get_one.json()
        print("====DETAIL OF A ID=====")
        print("User ID:", f_res_one["id"])
        print("User name:", f_res_one["username"])
        print("Email:", f_res_one["email"])
        print("City:", f_res_one["address"]["city"])
        print("Street:", f_res_one["address"]["street"])
    else:
        print("Enter a correct ID")

""" Post request """
    
payload = {
    "id": 11,
    "name": "Ervin Howel",
    "username": "Antonett",
    "email": "Shanna@melissaa.tv",
    "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "geo": {"lat": "-43.9509", "lng": "-34.4618"},
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains",
    },
}

def create_user():
    url_post = "https://jsonplaceholder.typicode.com/users"
    response_post = requests.post(url_post, json=payload)
    if response_post.status_code in (200, 201):
        f_pos = response_post.json()
        print(f_pos)
        print("Created successfully")
    else:
        print("Incorrect data")

""" Query parameter """

def get_from_query():
    url_get = "https://jsonplaceholder.typicode.com/users"
    parameter = {"username": "Antonette"}
    response_get_query = requests.get(url_get, params=parameter)
    f_res_query = response_get_query.json()
    print(f_res_query)
    print("No of user returned: ", len(f_res_query))

while True:
    print("\n==== MENU OPTIONS ====")
    print("1. Get all users")
    print("2. Get one user")
    print("3. Create user")
    print("4. Search user")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
          get_user()
        case 2:
          get_one_user()
        case 3:
          create_user()
        case 4:
          get_from_query()
        case 5:
          print("Exiting.......")
          break
        case _:
          print("Enter a valid choice")
        
        
    
