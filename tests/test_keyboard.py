from src.keyboard import Keyboard


class TestKeyboard:

    def test_init_keyboard(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert kb.name == 'Dark Project KD87A'
        assert kb.price == 9600
        assert kb.quantity == 5

    def test_str_keyboard(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert str(kb) == 'Dark Project KD87A'
