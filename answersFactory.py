# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:52:47 2022

@author: Aryan Shrivastava
"""
from s2t_1 import speechToText
from write import Writer


class Factory(speechToText,Writer):
    def __init__(self):
        pass
    #     self.model_name="sriAryan18/tf_bert_uncased_emotion_detection2"
    #     self.classifier=pipeline("text-classification",model=self.model_name, return_all_scores=True)
    def getObject(self,n):
        n=int(n)
        if(n==1):
            return Writer()
        elif n==2:
            
            # classifier=pipeline("text-classification",model=self.model_name, return_all_scores=True)
            return speechToText()
        else:
            print("Invalid Input")
            return None
            
  
            
    