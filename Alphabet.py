# coding: utf8
"""
Эта библиотека включает в себя самые распространенные алфавиты в мире. Буквы в нем расположены в обычном словарном
порядке, как принято обучать в школах.
Если вдруг Вы столкнетесь с задачей быстро сформировать лист букв, то можете ею воспользоваться.

Методы:
upperсhars()
lowerсhars()
uninumber(char)
"""


class Alphabet(object):

    def __init__(self, name, chars, chartype, codenumbers, description):
        """

        :param name: Название алфавита (на англ и русском)
        :param chars: Список букв алфавита
        :param chartype: Тип букв
        :param codenumbers: Код букв алфавита
        :param description: Описание (на англ и русском)
        """
        self.name = name
        self.chars = chars
        self.chartype = chartype
        self.codenumbers = codenumbers
        self.description = description
    def upperсhars(self):
        """

        :return: Возвращает список из букв в верхнем регистре или исключение
        """
        if self.chartype == "Letters":
            listupper = []
            for char in self.chars:
                if char.isupper():
                    listupper.append(char)
            return listupper
        else:
            raise Exception('This alphabet don\'t have upper chars')

    def lowerсhars(self):
        """

        :return: Возвращает список из букв в нижнем регистре или исключение
        """
        if self.chartype == "Letters":
            listlower = []
            for char in self.chars:
                if char.islower():
                    listlower.append(char)
            return listlower
        else:
            raise Exception ('This alphabet don\'t have lower chars')

    def uninumber(self, char):
        """

        :param char: Буква, номер которой ищем
        :return: Если буква присутствует в алфавите возвращает код, иначе исключение
        """
        if char in self.chars:
            return ord(char)
        else:
            raise Exception ('Wrong alphabet')

    def description(self,lang,what):
        """
        :param lang: на каком языке отображать информацию ('ru','en')
        :param what: что отобразить(ключ к словарю) ('name','about','all')
        :return: В зависимости от выбранных параметров возвращает информацию
        """
        if lang == "ru":
            if what == "name":
                return self.name["ru"]
            elif what == "about":
                return self.about["ru"]
            elif what == "all":
                return self.name["ru"],self.about["ru"]
            else:
                raise Exception("I don't understand what you want")
        elif lang == "en":
            if what == "name":
                return self.name["en"]
            elif what == "about":
                return self.about["en"]
            elif what == "all":
                return self.name["en"], self.about["en"]
            else:
                raise Exception("I don't understand what you want")




class Avestan(Alphabet):
    def __init__(self):
        self.name = {"en":"Avestan","ru":"Авестийский"}
        self.chartype = "Not letter"
        self.chars = [chr(char) for char in range(68352, 68406)]
        self.special_symbols = [chr(char) for char in range(68409, 68415)]
        self.about = {"ru" : "Авестийский алфавит служил для перезаписи Авесты — собрания священных текстов зороастрийцев. Эти книги были написаны на умершем, примерно, в V веке, авестийском языке. За основу алфавита было взято арамейское письмо, использовавшееся иранской шахской династией пехлеви. Состав алфавита изменялся в небольших пределах, в зависимости от конкретного переписчика. Старейшая сохранившаяся рукопись датируется XIII веком.","en" : "No desctiption"}



class Limbu(Alphabet):
  # Не уверен в точности символов.
  def __init__(self):
    self.name = {"en":"Limbu","ru":"Лимбу"}
    self.chartype = "Not letters"
    self.codenumbers = [i for i in range(6400,6443)]+[6464]
    self.chars = [chr(char) for char in self.codenumbers]
    self.about = {"ru":"С помощью алфавита лимбу записывают язык народности лимбу, которая проживает Непале, Сиккиме, Кашмире. Многие из этих людей, свободно говорят и пишут по-непальски, и при этом не владеют письмом лимбу.Этот алфавит произошёл от тибетского и является абугидой.",
                 "en":"Need translation"}

	
class Lepcha(Alphabet):
	def __init__(self):
		self.name = {"en":"Lepcha", "ru":"Лепча"}
		self.chartype = "Not letters"
		self.codenumbers = [i for i in range(7168,7247)]
		self.chars = [chr(char) for char in self.codenumbers]
		self.about = {"ru" : "Алфавит лепча использовался для записи языка народности лепча, которая проживает в индийском штате Сикким. Эта абугида произошла от тибетского письма в начале XVIII века. В настоящий момент, наверно, не применяется. Изначально, буквы записывались сверху вниз, но потом стали писаться горизонтально. Символы, при этом, не были повёрнуты на 90 градусов. Это сформировало необычный набор концевых согласных.", 
								 "en" : "Need translation"}


class Belorussian(Alphabet):
    def __init__(self):
        self.name = "Belorussian"
        self.chartype = "Letters"
        self.codenumbers = [i for i in range(1040, 1046)]+[1025]+[i for i in range(1046,1048)]+[1030]+\
                           [i for i in range(1049,1060)]+[1038]+[i for i in range(1060,1065)]+\
                           [i for i in range(1067,1072)]+[i for i in range(1072,1078)]+[1105]+\
                           [i for i in range(1078,1080)]+[1110]+[i for i in range(1081,1092)]+[1118]+\
                           [i for i in range(1092,1097)]+[i for i in range(1099,1104)]
        self.chars = [chr(char) for char in self.codenumbers]


class Bashkir(Alphabet):
    def __init__(self):
        self.name = "Bashkir"
        self.chartype = "Letters"
        self.description = "Современный башкирский алфавит утверждён в 1939 году. Введён в употребление годом позже. В 1950 в него была добавлена буква Ё, и он стал таким, какой он сейчас. Башкирский алфавит составлен на основе кириллицы, но дополнен девятью буквами для передачи специфичных звуков башкирского языка.\n"+"Всего содержит 42 буквы, две из которых уникальны, то есть, их нет больше ни в одной письменности.В древние времена, башкиры пользовались древнетюркским руническим письмом. Затем, с Х века, по мере распространения ислама – писали на арабском. С XIII по XIX века вели записи применяя старотюркский письменно-литературный язык. Он тоже был основан на арабском письме. В XIX – ХХ веках было насколько попыток создать национальный башкирский алфавит. Однако, ни одна из этих письменностей не использовалась достаточно долго."
        self.codenumbers = [i for i in range(1040,1044)]+[1170,1044,1176,1045,1025]+[i for i in range(1046,1051)]+[1184]\
                           +[i for i in range(1051,1054)]+[1186,1054,1256]+[i for i in range(1055,1058)]\
                           +[1194,1058,1059,1198,1060,1061,1210]+[i for i in range(1062,1070)]+[1240,1070,1071]\
                           +[i for i in range(1072,1076)]+[1171,1076,1177,1077,1105]+[i for i in range(1078,1083)]\
                           +[1185]+[i for i in range(1083,1086)]+[1187,1086,1257]+[i for i in range(1087,1090)]\
                           +[1195,1090,1091,1199,1092,1093,1211]+[i for i in range(1094,1102)]+[1241,1102,1103]
        self.chars = [chr(char) for char in self.codenumbers]


class Turic(Alphabet):
    def __init__(self):
        self.name = "Turic"
        self.chartype = "Rune"
        self.description = "Древнетюркский рунический алфавит был распространён в средней Азии в VIII-X веках. С его помощью писали на тюркских языках. Буквы названы рунами за сходство с германскими символами. Другое название письменности — орхонто-енисейская. Дано по местам археологических находок (долина Орхон и верховья Енисея).\n"+"Происхождение тюркских рун не установлено. По разным версиям, основой для них могли стать семитская письменность, кхароштхи, фонетические знаки китайского письма, родовые знаки тамга, согдийское письмо. По мере распространения ислама, тюркские руны были вытеснены арабским алфавитом."
        self.codenumbers = [i for i in range(68608,68680)]
        self.chars = [chr(char)for char in self.codenumbers]


class Russian(Alphabet):
    def __init__(self):
        self.name = 'Russian'
        self.chartype = "Letters"
        self.codenumbers = [i for i in range(1040, 1047)] + [1025] + [i for i in range(1047, 1078)] + [1105] + \
                      [i for i in range(1078, 1104)]
        self.chars = [chr(char) for char in self.codenumbers]


class English(Alphabet):
    def __init__(self):
        self.name = "English"
        self.chartype = "Letters"
        self.chars = [chr(char) for char in range(65,123) if 'a' <= chr(char) <= 'z' or 'A' <= chr(char) <= 'Z']

class German(Alphabet):
    def __init__(self):
        self.name = "German"
        self.codenumbers = [65, 196, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 214, 80, 81, 82, 83, 7838,
                            84, 85, 220, 86, 87, 88, 89, 90, 97, 228, 98, 99, 100, 101, 102, 103, 104, 105, 106,107,108,
                            109, 110, 111, 246, 112, 113, 114, 115, 223, 116, 117, 252, 118, 119, 120, 121, 122]
        self.chars = [chr(char) for char in self.codenumbers]
        self.chartype = "Letters"


class Spanish(Alphabet):
    def __init__(self):
        self.name = "Spanish"
        self.chartype = "Letters"
        self.codenumbers = [i for i in range(65, 79)]+[209]+[i for i in range(79, 91)]+[i for i in range(97,111)]+[241]+\
                           [i for i in range(111,123)]
        self.chars = [chr(char) for char in self.codenumbers]


class Italian(Alphabet):
    def __init__(self):
        self.name = "Italian"
        self.chartype = "Letters"
        self.codenumbers = [i for i in range(65, 74)]+[i for i in range(76, 87)]+[i for i in range(97, 106)] + \
                      [i for i in range(108, 119)]+[224, 232, 233, 236, 237, 238, 242, 243, 249, 250]
        self.chars = [chr(char) for char in self.codenumbers]


class Bulgarian(Alphabet):
    def __init__(self):
        self.name = "Bulgarian"
        self.chartype = "Letters"
        self.codenumbers = [i for i in range(1040, 1067)]+[1068, 1070, 1071]+[i for i in range(1072, 1099)]+ \
                      [1100, 1102, 1103]
        self.chars = [chr(char) for char in self.codenumbers]


class Greek(Alphabet):
    def __init__(self):
        self.name = "Greek"
        self.chartype = "Greek letters"
        self.codenumbers = [i for i in range(913, 938)]+[i for i in range(945, 970)]
        self.chars = [chr(char) for char in self.codenumbers]

class Glagolitic(Alphabet):
    def __init__(self):
        self.name = "Glagolitic"
        self.chartype = "Rune"
        self.description = "Глаголица — первая азбука (алфавит) славянских народов. Её составили Кирилл и Мефодий примерно в 863 году по приказу византийского императора Михаила III. Целью создания был перевод церковных текстов на древнеславянский язык.\n"+"Существует несколько аргументов в пользу того, что глаголица старше кириллицы. Старейшие рукописи написаны на ней, например, «Киевские листки», датируемые X веком. Также, до нас дошли некоторое количество пергаментов, на которых старый текст был соскоблен и нанесён новый (палимпсесты). Во всех случаях стёрта была глаголица. В своих старейших версиях кириллическая и глаголическая азбука почти полностью совпадают, различаясь начертанием символов. Хотя, отличаются и цифровые значения букв. В кириллице они соотносятся с греческими, а в глаголице с порядком букв в алфавите.\n"+"Сложно сказать откуда пошло начертание букв глаголицы. Есть сходство с грузинским церковным письмом, с греческой скорописью, и с древнетюркскими рунами. Существует версия, что Кирилл вдохновлялся рунической письменностью, которой славяне пользовались до этого. Однако убедительных доказательств этому нет.\n"+"В Древней Руси глаголица применялась редко. В рукописных памятниках можно увидеть только отдельные буквы в кириллических текстах. Большее распространение она получила в Болгарии и Хорватии. В основном использовалась священнослужителями. В Болгарии шрифт был округлый, а в Хорватии более угловатый."
        self.codenumbers = [i for i in range(11264,11306)]
        self.chars = [chr(char) for char in self.codenumbers]
