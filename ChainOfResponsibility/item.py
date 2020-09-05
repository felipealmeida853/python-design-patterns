class Item:

    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @nome.setter
    def nome(self, value):
        self._nome = value

    @valor.setter
    def valor(self, value):
        self._valor = value