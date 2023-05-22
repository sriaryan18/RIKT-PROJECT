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
    res=[]
    print(data)
    for keys in data.keys():
        print(data[keys])
        res.append(mlModel.get_prediction(data[keys]))



    return res # return the results 


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=3003,debug=True)
