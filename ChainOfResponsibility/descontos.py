import abc

from ChainOfResponsibility.orcamento import Orcamento


class Desconto(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def desconta(self):
        pass

    @abc.abstractmethod
    def set_proximo_desconto(self, proximo):
        pass


class DescontoPorCincoItens(Desconto):

    def __init__(self, orcamento: Orcamento , proximo: Desconto):
        self._orcamento = orcamento
        self._proximo = proximo

    def desconta(self):
        if len(self._orcamento.items) > 5:
            return self._orcamento.get_valor() * 0.1
        else:
            return self._proximo.desconta()

    def set_proximo_desconto(self, proximo: Desconto):
        self._proximo = proximo


class DescontoPorMaisQuinhentosReais(Desconto):

    def __init__(self, orcamento: Orcamento, proximo: Desconto):
        self._orcamento = orcamento
        self._proximo = proximo

    def desconta(self):
        if self._orcamento.get_valor() > 500:
            return self._orcamento.get_valor() * 0.07
        else:
            return self._proximo.desconta()

    def set_proximo_desconto(self, proximo: Desconto):
        self._proximo = proximo


class SemDesconto(Desconto):

    def __init__(self, orcamento: Orcamento):
        self._orcamento = orcamento

    def desconta(self):
        return 0

    def set_proximo_desconto(self):
        pass