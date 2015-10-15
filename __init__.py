# -.- coding: utf-8 -.-
from Modulos.STT_iteracao_por_fala.Sintetizador_Offline_eSpeak.SintetizadorThread import ThreadSintetizador as ths
from Modulos.TTS_reconhecedor_de_voz.ReconhecedorThread import ThreadReconhecimento as thr

#definir instancias de objetos com suas threads
#Feedback ao usuario que o sistema está iniciando -sintetizador de voz TTS
sintetizador = ths("sintetizador","Aguarde! O sistema está sendo iniciado!")
#reconhecedor STT
reconhecedor = thr("reconhecedor")
#iniciar as intancias de thread
sintetizador.start()
reconhecedor.start()
#feedback ao usuario que o sistema já está funcionando -sintetizador de voz TTS
sintetizador = ths("sintetizador","Aguarde! O sistema está sendo iniciado!")
sintetizador.start()
