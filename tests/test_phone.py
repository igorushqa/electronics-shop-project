import pytest

from src.phone import Phone


class TestPhone:

    def test_init_phone(self, phone):
        assert phone.name == "iPhone 14"
        assert phone.price == 120000
        assert phone.quantity == 5
        assert phone.number_of_sim == 2

    def test_repr_phone(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

    def test_str_phone(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert str(phone1) == 'iPhone 14'

    def test_number_of_sim(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 0)
        assert phone1.number_of_sim == 0
