# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 12:55:12 2022

@author: Aryan Shrivastava
"""

class Answers:
    def __init__(self,model):
        self.model=model
        self.results=None
        self.text_list=[]
    def set_text(self,text_list):
        self.text_list=text_list