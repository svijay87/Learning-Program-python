from pymongo import MongoClient
from pprint import pprint


client = MongoClient("mongodb://localhost:27017")

print(client)

db = client.rptutorials
print(db)

tutorial = db.tutorial


# for doc in tutorial.find():
#     pprint(doc)

jon_tutorial = tutorial.find_one({"author" : "Jon"})

pprint(jon_tutorial)

#Update reocrd
"""
res = tutorial.update_one({
    "author" : "Jon"},
    {
        "$set" : {
            "title" : "Updated title from update by pymongo",
            "url" : "https://realpython.com/introduction-to-mongodb-and-python/#using-mongodb-with-python-and-pymongo"
        }
    
})

pprint(res)
"""

# Delete

result = tutorial.delete_many({
    "author" : "Jon"
})

print(result.deleted_count)

client.close()