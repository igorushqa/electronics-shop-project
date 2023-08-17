from src.item import Item
from src.mixins import LangMixin


class Keyboard(Item, LangMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        LangMixin.__init__(self)

    def __str__(self):
        return f'{self.name}'
