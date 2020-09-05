import abc


class Impostos(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def calcula_imposto(self):
        pass
