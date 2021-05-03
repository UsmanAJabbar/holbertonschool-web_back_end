#!/usr/bin/env python3
from pprint import pprint


def list_all(mongo_collection):
    """ Lists all of the documents in a collection """
    return [doc for doc in mongo_collection.find()]
