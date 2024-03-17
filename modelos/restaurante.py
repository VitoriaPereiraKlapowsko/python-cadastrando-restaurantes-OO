from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante: #Criação de classe
    restaurantes = []
     
    def __init__(self, nome, _categoria): #Construtor o self é o .this
        self._nome = nome.title() #O title serve para colocar toda a primeira letra como maiusculo
        self._categoria = _categoria.upper() #O upper serve para colocar tudo em maiusculo
        self._ativo = False #Com o uso do _ eu estou querendo dizer que este atributo é privado
        self._avaliacao = []
        self._cardapio = []
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
    
    #def adicionar_bebida_no_cardapio(self, bebida): #Adicionando itens no cardapio de forma ruim
   #     self._cardapio.append(bebida)
        
   # def adicionar_prato_no_cardapio(self, prato):
    #    self._cardapio.append(prato)
    
     #Adicionando itens no cardapio de uma forma bem mais resumida com o isinstance
    def adiconar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #verificando se ele á um derivado da classe, assim pode colocar este item na lista
            self._cardapio.append(item)
            
    @property
    def exibir_cardapio(self): 
        print(f'Cardapio do Restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1): #coloquei um iteravel (i) e o enumerate para contar os indices na hora de listar os itens começando do 1 porque se não por padrão ele sempre vai iniciar em 0, fica como se fosse uma listinha 
            if hasattr(item, 'descricao'): #se tiver o atributo, ou seja se ele tiver uma descrição vai aparecer se não o programa não quebra
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)