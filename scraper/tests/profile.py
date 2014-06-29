# coding: utf-8
import unittest
from bson.objectid import ObjectId
from datetime import datetime
from scraper.models.profile import Profile


class TestProfile(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_profile(self):
        '''
        Tests if ORM abstraction layer is working for saving, retrieving and removing objects
        '''
        profile = Profile()
        profile._id = ObjectId()
        profile.name = "should-be-name"
        profile.username = "should-be-username"
        profile.short_description = "should-be-description"
        profile.image = "user profile image"
        profile.popularity = 10
        profile.updated = datetime(2014, 6, 29, 0, 35, 59, 152136)

        profile.save()

        profile_db = Profile().find_one({"username": profile.username})
        self.assertIsNotNone(profile_db)

        id_dict = {"_id": profile_db['_id']}
        profile_db['name'] = "should-be-name-updated"
        Profile().update(id_dict, profile_db)

        profile_db = Profile().find_one({"username": profile.username})
        self.assertEqual(profile_db['name'], "should-be-name-updated")

        Profile().remove({"username": profile.username})
        profile_db = Profile().find_one({"username": profile.username})
        self.assertIsNone(profile_db)