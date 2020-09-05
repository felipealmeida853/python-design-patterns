from interfaceImpostos import Impostos


class ICMS(Impostos):

    def __init__(self, orcamento):
        self._orcamento = orcamento

    def calcula_imposto(self):
        return self._orcamento.get_valor() * 0.1


class ISS(Impostos):

    def __init__(self, orcamento):
        self._orcamento = orcamento

    def calcula_imposto(self):
        return self._orcamento.get_valor() * 0.06