#!/usr/bin/env python3
"""Python script  """


def list_all(mongo_collection):
    """ List all documents in a collection  """

    return [doc for doc in mongo_collection.find()]
