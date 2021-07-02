import umongo
import asyncio
import pymongo
from dotenv import load_dotenv
import os
from umongo import Document, fields
from umongo.frameworks import PyMongoInstance
from marshmallow.exceptions import ValidationError
load_dotenv()

# !umongo
db = pymongo.MongoClient(os.getenv("DATABASE_URI"))['boom']

instance = PyMongoInstance(db)


collection = db['data']


@instance.register
class RMTian(Document):
    name = fields.StringField(required=True)
    discord_id = fields.IntegerField(unique=True)

    class Meta:
        collection_name = "data"

    async def is_registered(self=None, id=None):
        if id == None:
            return "Invalid ID"
        else:
            collection = db['data']
            number = collection.count_documents({"discord_id": id})
            if number >= 1:
                return True
            else:
                return False


async def register(name, id):
    if await RMTian.is_registered(id=id):
        return False
    else:
        rmtian = RMTian(name=name, discord_id=id)
        rmtian.commit()
        return True


async def remove_user(id):
    if await RMTian.is_registered(id=id):
        collection.delete_one({"discord_id": id})
        print("Done")
        return True
    else:
        return False
# collection = db['data']
# me = RMTian(name="Ash", discord_id=764415588873273345)
# if (collection.count_documents({"name": me.name})) >= 1:
#     print("User already exists")
# else:
#     me.commit()

# if db.collection.count_documents({ 'name': "Ash" }, limit = 1) != 0:
#
# collection.delete_many({})


# for i in RMTian.find({"name": "Ash"}):
#     print(i)
# print("Running")
# result = db['data'].find({"name": "hmm"})
# print("got result")
# print(result
# for i in result:
#     print("hmm")
#     print(i)


# def connect_mongo():

#     cluster = pymongo.MongoClient(
#         os.getenv("DATABASE_URI"))
#     db = cluster["test"]
#     instance
#     collection = db["test"]
#     return collection


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

if __name__ == "__main__":
    asyncio.run(remove_user(764180228369023006))
