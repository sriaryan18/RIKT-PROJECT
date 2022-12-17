# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 12:05:10 2022

@author: Aryan Shrivastava
"""

class Result:
    def __init__(self,model):
        self.model=model
        self.results=[]
    def get_results(self,listOfObj):
        for i in listOfObj:
            # print(i.get_inputted_data())
            self.results.append(self.model.get_prediction(i.get_inputted_data()))
        
            
    def show_results(self):
        print(self.results)