#!/usr/bin/env python3
"""Some random docstring"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts data into the school collection """
    return mongo_collection.insert_one(kwargs).inserted_id
