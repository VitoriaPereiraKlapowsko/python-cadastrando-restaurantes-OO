from abc import ABC, abstractmethod  #usando o conceito de classe abstrata

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @abstractmethod
    def aplicar_desconto(self):
       pass