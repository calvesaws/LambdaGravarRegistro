import sys
import json
from Services import MensagemService
from Dominio import Evento

def lambda_handler(event, context):

  evento = Evento.Evento(event['mensagem'],event['senha'], event['tempo'], event['visualizacoes_max'] );

  mensagem_service = MensagemService.MensagemService();

  mensagem_dto = mensagem_service.gravarMensagem(evento);

  resposta = mensagem_service.converte_json(mensagem_dto);
  
  return resposta
  
  
