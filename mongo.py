
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()


def connect_mongo():

    cluster = pymongo.MongoClient(
        os.getenv("DATABASE_URI"))
    db = cluster["test"]
    collection = db["test"]
    return collection
    

# collection.insert_one(data)
# to find data
# results = collection.find({"name": "Rishit"})
# for result in results:
#     print(result)

# Update data
# results = collection.update_one(
#     {"name": "Rishit"}, {"$set": {"github": "IamEinstein"}})
# delete
# results = collection.delete_one({"_id": 1})
# results = collection.delete_many({"name": "Rishit"})


# data count


# count = collection.count_documents({})
# print(count)
