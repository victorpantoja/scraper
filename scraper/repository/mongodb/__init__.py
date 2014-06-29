# coding: utf-8

import logging
from pymongo import MongoClient
#from webscraper import settings

__database__ = None

#TODO - FIX ME
database_url = "localhost"
database_port = 27017

def get_database():
    global __database__

    if not __database__:
        logging.info("MONGODB connecting database...")

        __database__ = MongoClient('mongodb://{0}:{1}'.format(database_url, database_port))['webscraper']

    return __database__
