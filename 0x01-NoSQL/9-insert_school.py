#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """function thar inserts a new document in a collection based on kwargs """
    value = mongo_collection.insert_one(kwargs)
    return value.inserted_id
