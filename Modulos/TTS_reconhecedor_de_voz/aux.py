#!/usr/bin/python
# -*- coding: UTF-8 -*-
#__________________________________________________________________________IMPORTS__________________________________________________________________________
import speech_recognition as sr
from bancodedados import BancoDeDados
import RPi.GPIO as GPIO  
#__________________________________________________________________________METODOS__________________________________________________________________________
#Metodo responsável pelo reconhecimento de voz
 
GPIO.setmode(GPIO.BOARD)  #using BOARD function, so that directly count off pin numbers in the header
 
GPIO.setup(8,GPIO.OUT)  #set pin to OUTPUT mode
def ouvir(r,source):
   print("buffer limpo")
   print("Pronto! estou a disposição!")
   audio = r.listen(source)
   return audio

def reconhecer(audio):
    print("Ok! Vou verificar...")
    try:
        return r.recognize_google(audio, key = None, language = "pt-BR", show_all = False)
    except sr.UnknownValueError:
        print("Oops! Nao Entendi")
    except RequestError:
        print "falha ao enviar"
    except LookupError:
        print("Oops! Nao Entendi")

def apresentarDadosTerminal(comando):
    if str is bytes: # this version of Python uses bytes for string (Python 2)
        print(u"Voce disse: {}".format(comando).encode("utf-8"))
    else: # this version of Python uses unicode for strings (Python 3+)
        print("Voce disse: {}".format(comando))

def consultarDispositivos():
    
    bd.execute("SELECT * FROM dispositivo")
    return bd.fetchall()

def consultarComandos():
    bd = BancoDeDados()
   # bd = conn.conexao
    resultado = bd.exSql("SELECT * FROM comando")
    return resultado.fetchall()
    return resultado

def reconhecerComandos(texto):
    #print u.encode('utf-8')
# tratar o texto.. Aqui tornamos o texto em um vetor de palavras semparando as pelo esplaco
    vetor = texto.split(" ")
    dispositivo =None
    comando=None
    for palavra in vetor:
        for result in consultarComandos():
	    if str(palavra) == result[1]:        
	        print("achou comando: "+str(result[1]))
	        if comando:
                    comando = comando +" "+result[1]
		    comando = comando.split(" ")
		else:
		    comando = result[1]
                break
        for result in consultarDispositivos():
           if str(palavra) == str(result[1]):
                print("achou comando: "+str(result[1]))
                if dispositivo:
                    dispositivo = dispositivo +" "+result[1]
                    dispositivo = dispositivo.split(" ")
                else:
                    dispositivo = result[1]
                break
    print str(comando)+" "+str(dispositivo)
    return str(comando)+" "+str(dispositivo)
	   
#______________________________________________________________________CHAMADA PRINCIPAL____________________________________________________________________
r = sr.Recognizer() 
print("Iniciando...")
with sr.Microphone() as source:
    pass
    r.adjust_for_ambient_noise(source)
    print("Regulando energia {}".format(r.energy_threshold))
    while True:
        ativar = True
        audio = ouvir(r, source)
        comando = reconhecer(audio)
        if comando:
            #reconhecerComandos(comando)
 	    apresentarDadosTerminal(comando)
            #reconhecerComandos(comando)
#	    gravarBd(format(comando))
	    if comando =="Acender luz":
		  GPIO.output(8,GPIO.HIGH)  #sending logic 1 to make the led high
 
 	          print "LED GOES ON"		
	    else:
		  GPIO.output(8,GPIO.LOW)  #sending logic 0 to make the led low
 
                  print "LED GOES OFF"		
class BancoDeDados:
    
    global conexao

    def __init__(self,local,usuario,senha,base):
        try:
            db = MySQLdb.connect(local,usuario, senha, base)
            conexao=db.cursor()
        except:
       	    print "Erro ao tentar se conectar com o banco de dados"

    
    
