#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:17:36 2023

@author: alexaowen
"""

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        test_object = BookLover("Alexa", "test@gmail.com", "thriller")
        
        test_object.add_book("The Paris Apartment", 4)
        
        self.assertEqual(test_object.book_list['book_name'][0], 'The Paris Apartment')
        self.assertEqual(test_object.book_list['book_rating'][0], 4)
    
    def test_2_add_book(self):
        test_object = BookLover("Alexa", "test@gmail.com", "thriller")
        
        test_object.add_book("Harry Potter and the Prisoner of Azkaban", 4)
        test_object.add_book("Harry Potter and the Prisoner of Azkaban", 4)
        
        self.assertEqual(list(test_object.book_list['book_name']).count("Harry Potter and the Prisoner of Azkaban"), 1)
    
    def test_3_has_read(self): 
        test_object = BookLover("Alexa", "test@gmail.com", "thriller")
        test_object.add_book("The Paris Apartment", 4)
        
        test_object.has_read('The Paris Apartment')
        
        self.assertTrue(test_object.has_read('The Paris Apartment'))
        
    def test_4_has_read(self):
        test_object = BookLover("Alexa", "test@gmail.com", "thriller")
        test_object.add_book("The Paris Apartment", 4)
        
        test_object.has_read('The Guest List')
        
        self.assertFalse(test_object.has_read('The Guest List'))
        
    def test_5_num_books_read(self):
        test_object = BookLover("Alexa", "test@gmail.com", "thriller")
        test_object.add_book("The Guest List", 3)
        test_object.add_book("Nine Perfect Strangers", 3)
        test_object.add_book("Everything I Never Told You", 4)
        
        self.assertTrue(test_object.num_books_read())
    
    def test_6_fav_books(self):
        test_object = BookLover("Alexa", "test@gmail.com", "thriller")
        test_object.add_book("Harry Potter and the Scorcer's Stone", 2)
        test_object.add_book("Harry Potter and the Chamber of Secrets", 3)
        test_object.add_book("Harry Potter and the Goblet of Fire", 4)
        test_object.add_book("Harry Potter and the Order of the Pheonix", 4)
        
        fav =test_object.fav_books()
        
        self.assertFalse("Harry Potter and the Scorcer's Stone" in list(fav['book_name']))
        self.assertFalse("Harry Potter and the Chamber of Secrets" in list(fav['book_name']))
        self.assertTrue("Harry Potter and the Goblet of Fire" in list(fav['book_name']))
        self.assertTrue("Harry Potter and the Order of the Pheonix" in list(fav['book_name']))

if __name__ == '__main__':
    unittest.main(verbosity=3)