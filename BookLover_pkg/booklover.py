#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:16:44 2023

@author: alexaowen
"""
import pandas as pd


class BookLover():
    """
    class that contains information on the name, and number of books a person has read
    """
    
    def __init__(self, name= '', email='', fav_genre='', num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
                 self.name=name
                 self.email = email
                 self.fav_genre = fav_genre
                 self.num_books = num_books
                 self.book_list = book_list
                    
    def add_book (self, book_name, rating):    
        if book_name in self.book_list['book_name'].value_counts():
            return f"The book '{book_name}' already exists in {self.name}'s list."
        else:
            new_book = pd.DataFrame({'book_name': book_name, 'book_rating': rating}, index = [0])
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
    def has_read (self, book_name):
        if book_name in self.book_list['book_name'].value_counts():
            return True
        else:
            return False
        
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
