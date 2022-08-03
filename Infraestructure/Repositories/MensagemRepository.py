import sys
import boto3
sys.path.append('../')
from Dominio import Mensagem 
from Dominio import Evento
 

class MensagemRepository():

    def GravarMensagem(mensagem: Mensagem):
       try:  
           cliente = boto3.resource('dynamodb')
           tabela = 'Dados'
    
           tabela = cliente.Table(tabela)


           tabela.put_item(Item= {'Id': mensagem.id,'mensagem': mensagem.mensagem,'senha': mensagem.senha, 'tempo': str(mensagem.tempo), 'visualizacoes_max' : str(mensagem.visualizacoes_max), 'visualizacoes': str(mensagem.visualizacoes)})
           return mensagem
       except:
             raise Exception("Exception ao tentar salvar o documento no Dynamodb")


