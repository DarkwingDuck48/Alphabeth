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
        if self.chartype == "Letters":
            listupper = []
            for char in self.chars:
                if char.isupper():
                    listupper.append(char)
            return listupper
        else:
            return 'This alphabet don\'t have upper or lower chars'

    def lowerсhars(self):
        if self.chartype == "Letters":
            listlower = []
            for char in self.chars:
                if char.islower():
                    listlower.append(char)
            return listlower
        else:
            return 'This alphabet don\'t have upper or lower chars'

    def uninumber(self,char):
        if char in self.chars:
            return ord(char)
        else:
            return 'Wrong Language'


class Avestan(Alphabet):
    def __init__(self):
        self.name = "Avestan"
        self.chartype = "Not letter"
        self.chars = [chr(char) for char in range(68352, 68406)]
        self.special_symbols = [chr(char) for char in range(68409, 68415)]


class Russian(Alphabet):
    def __init__(self):
        self.name = 'Russian'
        self.chartype = "Letters"
        codenumbers = [i for i in range(1040, 1047)] + [1025] + [i for i in range(1047, 1078)] + [1105] + \
                      [i for i in range(1078, 1104)]
        self.chars = [chr(char) for char in codenumbers]


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


class Spanish(Alphabet):
    def __init__(self):
        self.name = "Spanish"
        self.chartype = "Letter"
        codenumbers = [i for i in range(65, 79)]+[209]+[i for i in range(79, 91)]+[i for i in range(97, 111)]+[241] + \
            [i for i in range(111,123)]
        self.chars = [chr(char) for char in codenumbers]


class Italian(Alphabet):
    def __init__(self):
        self.name = "Italian"
        self.chartype = "Letter"
        codenumbers = [i for i in range(65, 74)]+[i for i in range(76, 87)]+[i for i in range(97, 106)] + \
                      [i for i in range(108, 119)]+[224, 232, 233, 236, 237, 238, 242, 243, 249, 250]
        self.chars = [chr(char) for char in codenumbers]


class Bulgarian(Alphabet):
    def __init__(self):
        self.name = "Bulgarian"
        self.chartype = "Letter"
        codenumbers = [i for i in range(1040, 1067)]+[1068, 1070, 1071]+[i for i in range(1072, 1099)]+ \
                      [1100, 1102, 1103]
        self.chars = [chr(char) for char in codenumbers]


class Greek(Alphabet):
    def __init__(self):
        self.name = "Greek"
        self.chartype = "Greek letter"
        codenumbers = [i for i in range(913, 938)]+[i for i in range(945, 970)]
        self.chars = [chr(char) for char in codenumbers]

