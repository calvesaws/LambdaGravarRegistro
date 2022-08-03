import string
import sys
import datetime
import time
from Dominio import Mensagem 
from Dominio.Dto import MensagemDto 
from Dominio import Evento
from Infraestructure.Repositories import MensagemRepository
sys.path.append('Services/modules')
import rsa 
import uuid

class MensagemService():
   

      def gravarMensagem( self, evento: Evento.Evento):

           expiracao = self.calcular_expiracao(evento.tempo)
           mensagem_crypt = self.criptografar(evento.mensagem)
           senha_crypt = self.criptografar(evento.senha)

           mensagem = Mensagem.Mensagem(str(uuid.uuid4()),mensagem_crypt,senha_crypt,expiracao, 0,evento.visualizacoes_max );

           mensagem_repository = MensagemRepository.MensagemRepository.GravarMensagem(mensagem)

           mensagem_dto = MensagemDto.MensagemDto( mensagem_repository.id, evento.mensagem, evento.senha,
           time.strftime( '%d-%m-%Y %H:%M:%S'  ,time.localtime(mensagem_repository.tempo)), mensagem_repository.visualizacoes_max);
           
          
           return mensagem_dto

       
      def calcular_expiracao(self, tempo: int):
           delta= datetime.timedelta(minutes = tempo
           )
           expiracao = datetime.datetime.now() + delta
           epoch = int(expiracao.timestamp())
           return epoch

      def criptografar(self,mensagem: string):
             
             with open('Services/chave/public_key.pem', mode='rb') as public_file:
                chave = public_file.read()
                public_key = rsa.PublicKey.load_pkcs1(chave,'PEM');
      
             mensagem_cript = rsa.encrypt(mensagem.encode(), public_key) 
             return mensagem_cript
        
      def converte_json(self, mensagem_dto):
          body =   {
          'id': mensagem_dto.id,
          'senha': mensagem_dto.senha,
          'visualizacoes_max': mensagem_dto.visualizacoes_max,
          'minutos': mensagem_dto.tempo
    
             }
             
          return { 
        'statusCode': 200,
       "headers": {
      "Access-Control-Allow-Origin": "*",
       "Access-Control-Allow-Header": "Content-Type",
              "Access-Control-Allow-Methods": "OPTIONS,POST"
       },
        'body': body
             }
