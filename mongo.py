import pymongo
from dotenv import load_dotenv
import os
from utils.tz import IST, format_time, datetime_from_utc_to_local
from datetime import datetime
from umongo import Document, fields
from umongo.frameworks import PyMongoInstance
load_dotenv()

# !umongo
#  Basic setup
db = pymongo.MongoClient(os.getenv("DATABASE_URI"))['boom']

instance = PyMongoInstance(db)
collection = db['data']
polls = db['polls']
# User model


@instance.register
class RMTian(Document):
    """
    Model for each user
    """
    name = fields.StringField(required=True)
    discord_id = fields.IntegerField(unique=True)
    send_dm = fields.BooleanField(default=True)

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
        return True
    else:
        return False

# Poll Model


@instance.register
class PollModel(Document):
    """
    MongoDB model for a poll
    """
    class Meta:
        collection_name = "polls"

    title = fields.StringField(unique=False)
    reactions = fields.ListField(fields.StringField())
    channel_id = fields.IntegerField(required=True)
    start_time = fields.DateTimeField(required=True)
    end_time = fields.DateTimeField(required=True)
    content = fields.StringField(required=True)
    poll_id = fields.IntegerField(required=True, unique=True)
    ended = fields.BooleanField(default=False)
    winner = fields.StringField(unique=False, default="None")
    winner_reaction_count = fields.IntegerField(default=0)
    tie = fields.BooleanField(default=False)
    tie_reaction_list = fields.ListField(fields.StringField(), default=[])

    async def check_ended_polls(self=None):
        for poll in polls.find({'ended': False}):
            ended_list = []
            if IST.localize(datetime_from_utc_to_local(poll['end_time'])) <= datetime.now(tz=IST):
                ended_list.append(poll)
                polls.find_and_modify(query={"_id": poll['_id']}, update={
                    '$set': {'ended': True}})
            return ended_list
        else:
            return None


for user in collection.find():
    collection.find_and_modify(query={"_id": user['_id']}, update={
        "$set": {"send_dm": True}})
