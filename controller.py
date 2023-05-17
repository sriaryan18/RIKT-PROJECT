from flask import Flask,request,jsonify
import MLMODEL
import answersFactory
from transformers import pipeline

model_name="sriAryan18/tf_bert_uncased_emotion_detection2"
classifier=pipeline("text-classification",model=model_name, return_all_scores=True)


app = Flask(__name__)
answerObj=answersFactory.Factory()
mlModel=MLMODEL.model(model_name, classifier)
@app.post('/get-emotions-text')
def getEmotionText():
    data=request.json
    # process the data
    print(data)
    res=mlModel.get_prediction(data['text1'])
    print(res)



    return res # return the results 


@app.route('/')
def hello():
    return 'Hello, World!'
