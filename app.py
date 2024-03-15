from modelos.restaurante import Restaurante #Aqui é como funciona uma importação, onde da pasta modelos pegamos o arquivo restaurante e importamos a classe Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'Melhor pão da cidade')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()