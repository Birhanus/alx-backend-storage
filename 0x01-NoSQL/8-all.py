#!/usr/bin/env python3
"""Python script  """

import pymongo


def list_all(mongo_collections):
    """ List all documents in a collection  """
    for x in mongo_collections.find():
        return [x]
