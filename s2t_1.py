# -*- coding: utf-8 -*-
"""S2T_1.ipynb
    Owned by: Aryan
"""

# ! pip install SpeechRecognition
# ! pip install pyaudio
# !pip install pydub
# !pip3 install wavio
# !pip3 install scipy

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
# from answers import Answers
class speechToText():
    def __init__(self,path="recording1.wav"):
        self.path=path
        self.full_text="NO TEXT RECORDED"
        self.text_list=[]
        self.r=sr.Recognizer()


    def record(self,f=45000,dur=10):
        freq =  f#45000   #44100

        # Recording duration
        duration = dur
        #         print("recording 

        # Start recorder with the given values
        # of duration and sample frequency
        print("Recording Started for {} seconds".format(dur))
        recording = sd.rec(int(duration * freq),
                samplerate=freq, channels=2)

        # Record audio for the given number of seconds
        sd.wait()
        print("Recording Ended")

        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("recording0.wav", freq, recording)

        # Convert the NumPy array to audio file
        wv.write("recording1.wav", recording, freq, sampwidth=2)



    def get_large_audio_transcription(self):
        """
        Splitting the large audio file into chunks
        and apply speech recognition on each of these chunks
        """
        path=self.path
        # open the audio file using pydub
        sound = AudioSegment.from_wav(path)  
        # split audio sound where silence is 700 miliseconds or more and get chunks
        chunks = split_on_silence(sound,
            # experiment with this value for your target audio file
            min_silence_len = 500,
            # adjust this per requirement
            silence_thresh = sound.dBFS-14,
            # keep the silence for 1 second, adjustable as well
            keep_silence=500,
        )
        folder_name = "audio-chunks"
        # create a directory to store the audio chunks
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        # process each chunk 
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # recognize the chunk
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = self.r.record(source)
                # try converting it to text
                try:
                    text = self.r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    # print(chunk_filename, ":", text)
                    whole_text += text
                    self.text_list.append(text)
        # return the text for all chunks detected
        if(len(text)>=10):
            self.full_text=text
    def get_text(self):
       self.record(44100,5)
       self.get_large_audio_transcription()
    def get_inputted_data(self):
       return self.text_list

# path = "recording1.wav"
# obj=speechToText(path)
# obj.record(44100)
# obj.get_large_audio_transcription()
# obj.text_list


# ob=speechToText()
# ob.get_text()








