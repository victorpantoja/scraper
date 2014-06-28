# coding: utf-8
from bson.objectid import ObjectId
from datetime import datetime
import pybreaker
import requests
import simplejson
from scraper.repository import ProfileRepository, Property, Collection


class Profile(Collection, ProfileRepository):

    __collection__ = 'profile'

    _id = Property(ObjectId, "profile id")
    name = Property(unicode, "user name")
    username = Property(unicode, "username")
    short_description = Property(unicode, "user name")
    image = Property(unicode, "user profile image")
    popularity = Property(int, "user popularity")
    updated = Property(datetime, "updated time")

    def as_profile_dict(self):
        '''
        Gets a specific profile (i.e. Facebook Profile) and convert it into WebScraper Profile
        This method must be implemented by subclasses.
        '''


class Facebook(Profile):

    def get_url_profile(self, username):
        return "http://graph.facebook.com/v1.0/" + username

    def as_profile_dict(self, **kwargs):
        facebook_breaker = pybreaker.CircuitBreaker(fail_max=1, reset_timeout=60)
        response = facebook_breaker.call(requests.get,
                                         Facebook().get_url_profile(kwargs['username']),
                                         timeout=5)

        response_dict = simplejson.loads(response.content)

        #TODO: usar os atributos com self ou entai usar o __init__
        profile = Profile()
        profile._id = ObjectId()
        profile.name = response_dict['first_name'] + " " + response_dict['last_name']
        profile.username = response_dict['username']
        profile.short_description = "A web developer at globo.com"
        profile.image = "user profile image"
        profile.popularity = 10
        profile.updated = datetime.now()

        return profile


class Twitter(Profile):
    pass


# simply add new classes and implement as_profile_dict to add new places where scrap from