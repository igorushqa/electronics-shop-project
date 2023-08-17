class LangMixin:
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        return self

    def __str__(self):
        return f'{self.__language}'

    @property
    def language(self):
        return self.__language
