from modelos.restaurante import Restaurante #Aqui é como funciona uma importação, onde da pasta modelos pegamos o arquivo restaurante e importamos a classe Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Vitoria', 10)
restaurante_praca.receber_avaliacao('Gui', 9)
restaurante_praca.receber_avaliacao('Anne', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()