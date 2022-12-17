import answersFactory
import results
import MLMODEL
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

model_name="sriAryan18/tf_bert_uncased_emotion_detection2"
classifier=pipeline("text-classification",model=model_name, return_all_scores=True)


name=input("Enter your name: ")

print("Hello {} I hope you are doing good today. Lets start analyzing your mental health".format(name))

answerObj=answersFactory.Factory()
mlModel=MLMODEL.model(model_name, classifier)

print("Instructions: ")
print("1. For every question prompted to you can either choose to speek or write the answer ")
print("2. To write the answers manually press 1 else 2")
print("Let's Start:  ")


print("{} how are feeling today ?".format(name))
n=input("Enter 1 to write 2 to speak")
obj1=answerObj.getObject(n)
obj1.get_text()

print("{} how frequent do you laugh these days?".format(name))
n=input("Enter 1 to write 2 to speak")
obj2=answerObj.getObject(n)
obj2.get_text()
print("{} are you enjoying your life ?".format(name))
n=input("Enter 1 to write 2 to speak")
obj3=answerObj.getObject(n)
obj3.get_text()
print("{} which part of the day is your favourite ?".format(name))
n=input("Enter 1 to write 2 to speak")
obj4=answerObj.getObject(n)
obj4.get_text()
print("{} Describe your day in brief".format(name))
n=input("Enter 1 to write 2 to speak")

obj5=answerObj.getObject(n)
obj5.get_text()

result=results.Result(mlModel)
result.get_results([obj1,obj2,obj3,obj4,obj5])


result.show_results()





# path = "recording1.wav"
# obj=s2t_1.speechToText(path)
# obj.record(44100,)
# obj.get_large_audio_transcription()
# # obj.text_list



# obj.text_list








# objModel=MLMODEL.model(model_name,classifier)
# # l=['i have a feeling i kinda lost my best friend','hi there'] 
# # objModel.get_prediction(l)
# # obj.result


# objModel.get_prediction(obj.text_list)

