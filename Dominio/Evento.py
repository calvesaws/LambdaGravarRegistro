import string

class Evento():
    
    def __init__(self, mensagem: string, senha:string, tempo: int, visualizacoes_max: int):
        self.mensagem = mensagem
        self.senha = senha
        self.tempo = tempo
        self.visualizacoes_max = visualizacoes_max
        

    mensagem: string
    senha: string
    tempo: int
    visualizacoes_max: int





