# coding: utf8
"""
Эта библиотека включает в себя самые распространенные алфавиты в мире. Буквы в нем расположены в обычном словарном
порядке, как принято обучать в школах.
Если вдруг Вы столкнетесь с задачей быстро сформировать лист букв, то можете ею воспользоваться.

Методы:
upperсhars() - возвращает лист из букв алфавита ТОЛЬКО в верхнем регистре.
lowerсhars() - возвращает лист из букв алфавита ТОЛЬКО в нижнем регистре.
uninumber(char) - возвращает номер Unicode выбранной буквы из алфавита.
"""
# Основной класс (__init__ возможно использовать для формирования собственного алфавита)
class Alphabet:
    def __init__(self, name, chars, chartype):
        self.name = name
        self.chars = chars
        self.chartype = chartype
    def upperсhars(self):
        listupper = []
        for char in self.chars:
            if char.isupper():
                listupper.append(char)
        return listupper

    def lowerсhars(self):
        listlower = []
        for char in self.chars:
            if char.islower():
                listlower.append(char)
        return listlower

    def uninumber(self,char):
        if char in self.chars:
            return ord(char)
        else:
            return 'Wrong Language'

class Russian(Alphabet):
    def __init__(self):
        self.name = 'Russian'
        self.chars = [chr(char) for char in range(256,10000) if 'а' <= chr(char) <= 'я' or 'А' <= chr(char) <= 'Я']
        self.chartype = "Letters"
class English(Alphabet):
    def __init__(self):
        self.name = "English"
        self.chars = [chr(char) for char in range(65,123) if 'a' <= chr(char) <= 'z' or 'A' <= chr(char) <= 'Z']
        self.chartype = "Letters"
class German(Alphabet):
    def __init__(self):
        self.name = "German"
        codenumbers = [65, 196, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 214, 80, 81, 82, 83, 7838, 84,
                       85, 220, 86, 87, 88, 89, 90, 97, 228, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
                       110, 111, 246, 112, 113, 114, 115, 223, 116, 117, 252, 118, 119, 120, 121, 122]
        self.chars = [chr(char) for char in codenumbers]
        self.chartype = "Letters"
class Arabic(Alphabet):
    def __init__(self):
        self.name = "Arabic"
        self.chartype = "Not letters"
        codenumbers = [65166,]


