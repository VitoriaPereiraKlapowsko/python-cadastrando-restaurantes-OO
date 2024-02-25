class Restaurante: #Criação de classe
    restaurantes = []
     
    def __init__(self, nome, categoria): #Construtor o self é o .this
        self._nome = nome.title() #O title serve para colocar toda a primeira letra como maiusculo
        self.categoria = categoria.upper() #O upper serve para colocar tudo em maiusculo
        self._ativo = False #Com o uso do _ eu estou querendo dizer que este atributo é privado
        Restaurante.restaurantes.append(self) #Criei um objeto e a coloquei dentro de uma lista
        
    def __str__(self): # Serve para aparacer o que está escrito como Praça | Gourmet e outros com o uso do str
        return f'{self._nome} | {self.categoria}'
        
    def listar_restaurantes(): #Criando um método para listar os restaurantes, assim não preciso ficar dando um print toda hora para mostrar as informações
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')
            
    @property #Modifico a forma de como aquele atributo vai ser lido
    def ativo(self):
        return '☑' if self._ativo else '☐' #Usando o coolsymbol para colocar estes simbolos
    
#Instanciando a Classe
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
