#!/usr/bin/env python
# coding: utf-8



class model:
    def __init__(self,model_name,classifier):
        self.model_name=model
        self.classifier = classifier
        self.result=None
  
    def process_result(self):
        max_scores=[]
        
        for s in self.result:
            ms=1e-20
            for i in s:
                if ms<i['score']:
                    ms=i['score']
                    name=i['label']
            if ms<=0.3:
                name="Neutral"
            max_scores.append({"label":name,"score":ms})
        return max_scores
    
    
    def get_prediction(self,text_list):
        self.result=self.classifier(text_list)
        return self.process_result()
    
    
        


# model_name="sriAryan18/tf_bert_uncased_emotion_detection2"
# classifier=pipeline("text-classification",model=model_name, return_all_scores=True)

# obj=model(model_name,classifier)
# l=['i have a feeling i kinda lost my best friend','hi there'] 
# obj.get_prediction(l)
# obj.result


# In[21]:





# In[23]:


# !jupyter nbconvert MLMODEL.ipynb --to python


# In[ ]:




