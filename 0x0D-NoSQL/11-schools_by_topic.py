#!/usr/bin/env python3


def schools_by_topic(mongo_collection, topic):
    """Returns a list of dictionaries that contain a topic"""
    return [doc for doc in mongo_collection.find({'topic': topic})]
