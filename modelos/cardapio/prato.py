from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)  #Acessando informações de outra classe com o super..., herdando o nome e preço da classe main que é a item_cardapio
        self.descricao = descricao
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco *0.05) #o -= é uma abreviação do = self._preco - ()