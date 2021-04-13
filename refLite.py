from datetime import *
import speech_recognition as sr   
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
def speechrecog(x):
    
    
    AF = ( x+".wav" ) 
    
    r = sr.Recognizer()    
    with sr.AudioFile(AF) as src: 
       audio = r.record(src) 
    
    print("Converting")
    global S
    S = r.recognize_google(audio) 
    
    try:
        file = "E_for_" + str(datetime.now().day) + str(datetime.now().month) + "_at" + str(datetime.now().hour) + str(datetime.now().minute)
        f = open(file + ".txt", "w") 
        f.write(S)
        f.close()
        return "Done!"
    except sr.UnknownValueError:
        return "ME NO KNOW WUT YOU SAY"
    except sr.RequestError:
        return "SYSTEM DOWN, SOWIE"
    
def sentimentAnalysis(data):
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    ss = sia.polarity_scores(data)
    print("------------------------------------------------------------------------------------------")
    print("SENTENCE:", data)
    print("------------------------------------------------------------------------------------------")
        
    print(ss['compound'])
    
    

if __name__ == "__main__":
    fileName = input("Enter the name of the .wav file - ")
    print(speechrecog(fileName))
    sentimentAnalysis(S)

