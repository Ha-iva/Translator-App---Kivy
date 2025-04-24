import kivy
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.label import  Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from gtts import gTTS
import os
import httpcore
import httpx
import time
import playsound
import speech_recognition as sr
import pyaudio

trans=Translator()

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    t1=ObjectProperty(None)
    t2=ObjectProperty(None)
    t5=ObjectProperty(None)
    t6=ObjectProperty(None)
    spin1=ObjectProperty(None)
    spin2=ObjectProperty(None)
    
    def btn1(self):
        self.speak(self.t1.text)
        
    def btn2(self):
        self.speak(self.t2.text)
        
    def btn4(self,value):
        self.ids.t5.text=value
        
    def btn5(self,value):
        self.ids.t6.text=value
        
    def btn3(self):
        l=LANGUAGES
        a=self.t5.text
        a1=a.lower()
        b=self.t6.text
        b1=b.lower()
        l1=list(l.values()).index(a1)
        lang1=list(l.keys())[l1]
        l2=list(l.values()).index(b1)
        lang2=list(l.keys())[l2]
        self.translate_to(self.t1.text,lang1,lang2)
        
    def speak(self,text):
        tts = gTTS(text)
        filename='voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)     
        
    def translate_to(self,text,sou,des):
        send=self.ids['t2']     
        translated=trans.translate(text,dest=des,src=sou).text
        send.text=translated
        
    
class FourthWindow(Screen):
    t3=ObjectProperty(None)
    t4=ObjectProperty(None)
    def btn4(self):
        self.detect_lang(self.t3.text)
    def detect_lang(self,text):
        send1=self.ids['t4']   
        detect=trans.detect(text).lang
        lang_u=LANGUAGES[detect].title()
        send1.text=lang_u
        
    def btn5(self):
        self.get_audio()
    def get_audio(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            
            try:
                a_t=r.recognize_google(audio)
                send2=self.ids['t3']
                send2.text=a_t
                self.detect_lang(a_t)
            except Exception as e:
                print("Exception : "+str(e))

class WindowManager(ScreenManager):
    pass

kv=Builder.load_file("translator.kv")

class TranslatorApp(App):
    def build(self):
        self.icon="logo.png"
        return kv
        
    
if __name__=="__main__":
    TranslatorApp().run()
