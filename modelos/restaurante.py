from modelos.avaliacao import Avaliacao

class Restaurante: #Criação de classe
    restaurantes = []
     
    def __init__(self, nome, _categoria): #Construtor o self é o .this
        self._nome = nome.title() #O title serve para colocar toda a primeira letra como maiusculo
        self._categoria = _categoria.upper() #O upper serve para colocar tudo em maiusculo
        self._ativo = False #Com o uso do _ eu estou querendo dizer que este atributo é privado
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #Criei um objeto e a coloquei dentro de uma lista
        
    def __str__(self): # Serve para aparacer o que está escrito como Praça | Gourmet e outros com o uso do str
        return f'{self._nome} | {self._categoria}'
        
    @classmethod#Metodo que referencia a classe    
    def listar_restaurantes(cls): #Criando um método para listar os restaurantes, assim não preciso ficar dando um print toda hora para mostrar as informações
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: #O uso de Cls é por convenção
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')
            
    @property #Modifico a forma de como aquele atributo vai ser lido
    def ativo(self):
        return '☑' if self._ativo else '☐' #Usando o coolsymbol para colocar estes simbolos
    
    def alternar_estado(self): #Metodo para os objetos
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property #Ser capaz de ler cada uma dessas informações para cada restaurante
    def media_avaliacoes(self):
        if not self._avaliacao: #Se não tiver avaliação retorna um 0
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #Somando todas as notas
        quantidade_de_notas = len(self._avaliacao) #Pegando o tamanho
        media = round(soma_das_notas / quantidade_de_notas, 1) #Arredondando em 1 as casas decimais
        return media