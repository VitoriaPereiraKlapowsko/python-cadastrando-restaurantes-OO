class Restaurante: #Criação de classe
    restaurantes = []
     
    def __init__(self, nome, categoria): #Construtor o self é o .this
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #Criei um objeto e a coloquei dentro de uma lista
        
    def listar_restaurantes(): #Criando um método para listar os restaurantes, assim não preciso ficar dando um print toda hora para mostrar as informações
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
        
    def __str__(self): # Serve para aparacer o que está escrito como Praça | Gourmet e outros com o uso do str
        return f'{self.nome} | {self.categoria}'
    
#Instanciando a Classe
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
