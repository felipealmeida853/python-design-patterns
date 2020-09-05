class Orcamento:

    def __init__(self):
        self._valor = 0
        self._items = []

    def get_valor(self):
        return self._valor

    @property
    def items(self):
        return self._items

    def add_items(self, value):
        self._items.append(value)
        self._valor += int(value.valor)
