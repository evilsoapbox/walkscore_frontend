"""
Unit tests for the WsLocation class.
"""

# Imports
import unittest
from walkscore_frontend.wslocation import City
from walkscore_frontend.wslocation import Neighborhood
from walkscore_frontend.wslocation import WsLocation

class TestWsLocation(unittest.TestCase):
    """Class to test WsLocation"""

    def setUp(self):
        """
        Setup the unit tests
        
        :return: Items needed for unit testing
        """
        self.simple_city_test_payload = {'name': 'Seattle', 'state': 'WA'}
        self.simple_nh_test_payload = {'name': 'Denny Triangle', 'city': 'Seattle', 'state': 'WA'}

    def test_wslocation_creation(self):
        """
        Test the creation of a simple WsLocation
        
        :return: OK if all unit tests pass
        """
        ws_loc = WsLocation(self.simple_city_test_payload, {'population': 100000})
        self.assertTrue(ws_loc is not None)
        self.assertTrue(ws_loc.name == 'Seattle')
        self.assertTrue(ws_loc.state == 'WA')
        self.assertRaises(AttributeError, getattr, ws_loc, "invalid_attribute")
        self.assertEqual(ws_loc.population, 100000)

    def test_city_creation(self):
        """
        Test the creation of a simple City object
        
        :return: Pass if the city is created OK
        """
        city = City(self.simple_city_test_payload)
        self.assertTrue(city is not None)
        self.assertRaises(AttributeError, getattr, city, "bad_attribute")
        self.assertTrue(city.name == 'Seattle')
        self.assertTrue(city.state == 'WA')


    def test_nh_creation(self):
        """
        Test the creation of a simple test_city_creation
        
        :return: Pass if the city is created OK
        """
        nh = Neighborhood(self.simple_nh_test_payload)
        self.assertTrue(nh is not None)
        self.assertTrue(nh.name == 'Denny Triangle')
        self.assertTrue(nh.city == 'Seattle')
        self.assertTrue(nh.state == 'WA')
        self.assertRaises(AttributeError, getattr, nh, "bad_attribute")