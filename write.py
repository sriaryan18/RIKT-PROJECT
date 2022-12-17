# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 12:01:32 2022

@author: Aryan Shrivastava
"""

# from MLMODEL import model

class Writer():
    def __init__(self):
        self.text=""
    def get_text(self):
        self.text=input("Please start writing: ")
    def get_inputted_data(self):
        return self.text
    
    
        
        
        
# obj=Writer("xyz")