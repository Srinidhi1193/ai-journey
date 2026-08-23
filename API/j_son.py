""" java script object notation """
""" 

load   - load JSON from a file into a Python object
loads  - load JSON from a string into a Python object
dump   - dump a Python object into a JSON file
dumps  - dump a Python object into a JSON string

"""
import json
json_string = '''
{
    "persons": [
        {
            "id": 1,
            "name": "John",
            "age": 25,
            "city": "Chennai",
            "skills": ["Python", "SQL", "FastAPI"]
        },
        {
            "id": 2,
            "name": "Priya",
            "age": 28,
            "city": "Bangalore",
            "skills": ["Java", "Spring Boot", "AWS"]
        },
        {
            "id": 3,
            "name": "Rahul",
            "age": 23,
            "city": "Hyderabad",
            "skills": ["Python", "Django", "PostgreSQL"]
        }
    ]
}
'''
"""load a python string into json object"""

data = json.loads(json_string)
print(data)
for person in data['persons']:
    for key,value in person.items():
        print(key, " - ",value)

"""dump a json object into python string"""

for person in data['persons']:
    del person['city']

new = json.dumps(data, indent=2,sort_keys=True)
print(new)


"""load a file into json object"""

with open ('states.json','r') as f:
    info_data = json.load(f)

for states in info_data["states"]:
    del states["abbreviation"]

with open('new.json','w') as nf:
    json.dump(info_data,nf,indent=2,sort_keys=True)