class Player:
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol
