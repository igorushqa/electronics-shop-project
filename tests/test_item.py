from src.item import Item


class TestItem:
    def test_init_item(self, item):
        assert item.name == "Смартфон"
        assert item.price == 10000
        assert item.quantity == 20
        assert Item.all == [item]

    def test_calculate_total_price(self, item):
        assert item.calculate_total_price() == 200000

    def test_apply_discount(self, item):
        item.pay_rate = 0.8
        item.apply_discount()
        assert item.price == 8000

    def test_name(self):
        item = Item('Телефон', 10000, 5)
        item.name = 'Смартфон'
        assert item.name == 'Смартфон'
        item.name = 'СуперСмартфон'
        assert item.name == 'СуперСмарт'

    def test_string_to_number(self):
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5
        assert Item.string_to_number('5.5') == 5
