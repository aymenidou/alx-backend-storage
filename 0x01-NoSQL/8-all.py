#!/usr/bin/python3
def list_all(mongo_collection):
    """
    Fetches all documents from a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of dictionaries representing the documents in the collection.
        An empty list if no documents are found.
    """
    documents = list(mongo_collection.find())
    return documents
