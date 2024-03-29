from modelos.restaurante import Restaurante #Aqui é como funciona uma importação, onde da pasta modelos pegamos o arquivo restaurante e importamos a classe Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'Melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adiconar_no_cardapio(bebida_suco)
restaurante_praca.adiconar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()