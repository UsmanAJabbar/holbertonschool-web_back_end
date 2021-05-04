#!/usr/bin/python3
"""Some random docstring"""


def update_topics(mongo_collection, name, topics):
    """Changes the topics of a school document"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {
            "topics": topics
        }}
    )
