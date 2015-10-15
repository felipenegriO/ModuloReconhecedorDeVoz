#!/usr/bin/python
# -*- coding: UTF-8 -*-
import speech_recognition as sr
import time

class Reconhecedor():
    
    def __init__(self):
        r = sr.Recognizer()
        self.r = r
        print("Iniciando...")
        with sr.Microphone() as source:
            self.source = source
            pass
            r.adjust_for_ambient_noise(source)
            print("Regulando energia {}".format(r.energy_threshold))
            self.iniciarReconhecimento()       
            
    def iniciarReconhecimento(self):
        while True:
            audio = self.ouvir()
            comando = self.reconhecer(audio)
            #if comando:
            print(comando)
          
            
    def ouvir(self):
       audio = self.r.listen(self.source)
       return audio
    
    def reconhecer(self,audio):
        print("Ok! Vou verificar...")
        try:
            return self.r.recognize_google(audio, key = None, language = "pt-BR", show_all = False)
        except sr.UnknownValueError:
            print("Oops! Nao Entendi")
        except RequestError:
            print "falha ao enviar"
        except LookupError:
            print("Oops! Nao Entendi")
