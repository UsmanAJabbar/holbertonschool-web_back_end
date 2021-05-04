#!/usr/bin/env python3
"""Some random docstring"""


def list_all(mongo_collection):
    """ Lists all of the documents in a collection """
    return [doc for doc in mongo_collection.find()]
