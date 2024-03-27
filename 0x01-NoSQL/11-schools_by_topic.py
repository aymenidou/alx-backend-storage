#!/usr/bin/env python3
'''0x01-NoSQL'''


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that have a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic: The topic to search for (string).

    Returns:
        A list of school documents matching the search criteria.
    """
    filter = {"topics": {"$in": [topic]}}  # Use $in operator for list search
    return list(mongo_collection.find(filter))
