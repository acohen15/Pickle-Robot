"""
Author: Ariella Cohen
Date: 09/19/2019
Project: Pickle Robot Python Challenge

"""

import unittest
from pickle import *

class testpickle(unittest.TestCase):
    
    def test_words_to_number(self):

        """Test words_to_number function to make sure that it is returning the
        proper phone numbers for all wordified numbers."""
        self.assertEqual(words_to_number("1-800-CARPETS"),"1-800-227-7387", "should be '1-800-227-7387'")
        self.assertEqual(words_to_number("1-800-FUR-1830"),"1-800-387-1830", "should be '1-800-387-1830'")
        self.assertEqual(words_to_number("1-866-111-TREE"),"1-866-111-8733", "should be '1-866-111-8733'")
        self.assertTrue(words_to_number("1-800-22-BREAD") == "1-800-222-7323", "should be True")
        self.assertFalse(words_to_number("1-866-FLOWER-4") == "1-800-356-9374", "should be False")
        
unittest.main()
