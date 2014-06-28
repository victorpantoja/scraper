# coding: utf-8

import logging
from pymongo import MongoClient
from webscraper import settings

__database__ = None


def get_database():
    global __database__

    if not __database__:
        logging.info("MONGODB connecting database...")

        __database__ = MongoClient('mongodb://{0}:{1}'.format(settings.database_url,
                                                              settings.database_port))['webscraper']

    return __database__
