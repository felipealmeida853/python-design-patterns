from ChainOfResponsibility.orcamento import Orcamento
from ChainOfResponsibility.descontos import *
from ChainOfResponsibility.item import *


def calcula_desconto(orcamento: Orcamento):
    desconto_3 = SemDesconto(orcamento)
    desconto_2 = DescontoPorMaisQuinhentosReais(orcamento, desconto_3)
    desconto_1 = DescontoPorCincoItens(orcamento, desconto_2)

    return desconto_1.desconta()


def main():
    lapis = Item("lapis", 500)
    caneta = Item("Caneta", 800)
    orcamento = Orcamento()
    orcamento.add_items(lapis)
    orcamento.add_items(caneta)
    desconto = calcula_desconto(orcamento)
    print(desconto)


if __name__ == '__main__':
    main()