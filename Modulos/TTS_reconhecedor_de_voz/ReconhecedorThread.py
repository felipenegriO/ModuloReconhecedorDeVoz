# -.- coding: utf-8 -.-
from threading import Thread
from SpeechRecognition import Reconhecedor as sr
class ThreadReconhecimento(Thread):
        #sobrescrita do metodo init
        def __init__ (self,argumento):
            Thread.__init__(self)
            self.argumento = argumento
            
        def run(self):
            reconhecedor = sr()
            reconhecedor.iniciarReconhecimento()
