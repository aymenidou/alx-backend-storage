#!/usr/bin/env python3
'''0x01-NoSQL'''


def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document into a MongoDB collection using keyword arguments.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Keyword arguments representing the document fields.

    Returns:
        The ObjectId of the inserted document.
    '''
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
