# -.- coding: utf-8 -.-
from threading import Thread
from Sintetizador import Sintetizador as sin
class ThreadSintetizador(Thread):
        #sobrescrita do metodo init
        def __init__ (self,argumento,texto):
            Thread.__init__(self)
            self.texto = texto
            self.argumento = argumento
            
        def run(self):
            sintetizador = sin(self.texto)
