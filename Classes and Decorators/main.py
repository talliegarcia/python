import sys
from datetime import datetime
import argparse
import random


# класс создается при помощи ключевого слова class
# в классе могут быть как методы, так и значения. По умолчанию они все публичные!
# если хотите скрыть какие-либо методы или переменные класса - давайте им названия с двойным подчеркиванием впереди:
# def __private_method()
# при написании кода для класса в метод первым параметром всегда передается self - указатель на сам класс
# при искользовании членов класса в коде класса обращайтесь к ним через self: self.__args
class Parser():
    __parser = None
    __args = None

    def __init__(self, sysargs):
        self.__parser = self.__create_parser()
        self.__args = vars(self.__parser.parse_args(sysargs))
        print(f"Аргументы командной строки внутри класса: {self.__args}")

    def __create_parser(self):
        parser = argparse.ArgumentParser(description="main.py -digits [--fullmatch_sign --match_sign")
        parser.add_argument("-digits", type=int, default=4, help="")
        parser.add_argument("--fullmatch_sign", type=str, default="B", help="")
        parser.add_argument("--match_sign", type=str, default="K", help="")

        return parser

    @property
    def show_args(self):
        return self.__args

    def New_Game(self):
        Start = Game(self.__args["digits"], self.__args["fullmatch_sign"], self.__args["match_sign"])
        return Start


def main():
    class_parser = Parser(sys.argv[1:])
    print(f"Аргументы командной строки вне класса: {sys.argv}")
    Round(class_parser.New_Game())


class Gamer():
    __history = None
    __counter = 0

    def __init__(self):
        self.__counter = 0
        self.__history = dict()

    def next_move(self):
        user_number = self.__get_user_number()
        self.__counter += 1
        self.__history[self.__counter] = {"user_number": user_number,
                                          "match_result": ""}
        return user_number

    def set_result(self, result):
        self.__history[self.__counter]["match_result": result]

    def __get_user_number(self):
        user_number = input("Введите число: ")
        if user_number.isdecimal():
            return user_number
        else:
            print("Вы ввели не число")
            return "0000"


class Game():
    __fullmatch = ""
    __match = ""
    __digits = 4
    digits_public = 4
    __number = "0000"

    def __rand_generator(self, digits):
        random.seed()
        s = ""
        for r in range(digits):
            s += str(random.randrange(10))
        # s=str(8208)
        # print (s)
        return s

    def __init__(self, digits, fullmatch, match):
        self.fullmatch = fullmatch
        self.match = match
        self.digits = digits
        self.digits_public = digits
        self.number = self.__rand_generator(digits)

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def digits(self):
        return self.__digits

    @digits.setter
    def digits(self, value):
        self.__digits = value

    @property
    def fullmatch(self):
        return self.__fullmatch

    @fullmatch.setter
    def fullmatch(self, value):
        self.__fullmatch = value

    @property
    def match(self):
        return self.__match

    @match.setter
    def match(self, value):
        self.__match = value


class Round():
    __game = None
    __gamer = None

    def __init__(self, game):
        self.__game = game
        self.__gamer = Gamer()
        self.worker()

    def __compare(self, number, user_number):
        # 1) сравнить
        if number == user_number:
            return 1
        if len(number) != len(user_number):
            print(f"Введите {len(number)} цифр(ы)")
            return 0
        else:
            result = list()
            buf = list()
            for i in range(len(number)):
                if number[i] == user_number[i]:
                    result.append(self.__game.fullmatch)
                    buf.append("*")
                else:
                    buf.append(str(number[i]))
            for i in range(len(number)):
                if user_number[i] in buf:
                    result.append(self.__game.match)
                    # print (buf)
                    a = buf.index(user_number[i])
                    buf[a] = ('~')
            result = "".join(result)
            # 2) выдать результат сравнения - print
            print(result)
            return 0

    def worker(self):
        n1 = self.__game.number
        while True:
            n2 = self.__gamer.next_move()
            won = self.__compare(n1, n2)
            if won:
                print("Вы победили")
                break


if __name__ == "__main__":
    main()
