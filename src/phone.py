from src.item import Item


class Phone(Item):
    """
    класс `Phone` содержит все атрибуты класса `Item`
    и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


