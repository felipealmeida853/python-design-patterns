from tiposImpostos import *
from orcamento import *


def calcula_imposto(imposto):
    print(imposto.calcula_imposto())


def main():
    orcamento_filial = Orcamento(550)
    icms = ICMS(orcamento_filial)
    iss = ISS(orcamento_filial)
    calcula_imposto(icms)
    calcula_imposto(iss)


if __name__ == "__main__":
    main()
