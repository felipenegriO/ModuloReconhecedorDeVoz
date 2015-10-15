#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
class Sintetizador(object):
    #classe de sintetização de voz

    def __init__(self, texto):
        self.texto = texto
     	self.sintetizar(texto)
     	
    def sintetizar(self,texto):
	print "teste"
        os.system("espeak -v pt -s 100 '" + texto + "'")
        
