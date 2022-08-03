import string

class MensagemDto():
    
    def __init__(self,id: string, mensagem: string, senha:string, tempo: int, visualizacoes_max: int):
        self.id = id
        self.mensagem = mensagem
        self.senha = senha
        self.tempo = tempo
        self.visualizacoes_max = visualizacoes_max

    
    id: string
    mensagem: string
    senha: string
    tempo: int
    visualizacoes_max: int





