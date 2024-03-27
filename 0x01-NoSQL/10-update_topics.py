#!/usr/bin/env python3
def update_topics(mongo_collection, name, topics):
    """
    Updates the topics field of a school document based on the name.

    Args:
        mongo_collection: A pymongo collection object.
        name: The name of the school document to update (string).
        topics: The new list of topics to be assigned (list of strings).
    """
    filter = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_one(filter, update)
