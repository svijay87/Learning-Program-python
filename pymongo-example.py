from pymongo import MongoClient
from pprint import pprint


client = MongoClient("mongodb://localhost:27017")

print(client)

db = client.rptutorials
print(db)

tutorial = db.tutorial

rec = {
    "title": "Working With JSON Data in Python",
    "author": "Lucas",
    "contributors": [
        "Aldren",
        "Dan",
        "Joanna"
    ],
    "url": "https://realpython.com/python-json/"
}

res = tutorial.insert_one(rec)
print(res)
print(f"One tutorial: {res.inserted_id}")

rec2 = {
    "title": "Python's Requests Library (Guide)",
    "author": "Alex",
    "contributors": [
        "Aldren",
        "Brad",
        "Joanna"
    ],
    "url": "https://realpython.com/python-requests/"
}

rec3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": [
        "Aldren",
        "Joanna",
        "Jacob"
    ],
    "url": "https://realpython.com/python3-object-oriented-programming/"
}

response = tutorial.insert_many([rec2,rec3])

print(f"response Ids : {response.inserted_ids}")


for doc in tutorial.find():
    pprint(doc)

jon_tutorial = tutorial.find_one({"author" : "Jon"})

pprint(jon_tutorial)

client.close()