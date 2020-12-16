from ._utility import num2char, char2num, staticproperty

class Rotor():
    __max_position = 26
    def __init__(self, right, left):
        self.__position = 0
        self.__offset = char2num(right[0])
        self.__right_to_left = {}
        self.__left_to_right = {}
        for r,l in zip(right.lower(), left.lower()):
            self.__right_to_left[r] = l
            self.__left_to_right[l] = r
    def advance(self):
        self.__position = (self.__position + 1) % Rotor.__max_position
        return self.__position == 1
    def set_initial_letter(self, letter):
        delta = (char2num(letter) - self.__offset) % Rotor.__max_position
        self.__position = (self.__position + delta) % Rotor.__max_position
    def set_offset(self, offset):
        self.__offset = (self.__offset - offset) % Rotor.__max_position
    def __encode(self, pos, dict):
        idx = (pos + self.__offset + self.__position) % Rotor.__max_position
        return (char2num(dict[num2char(idx)]) - self.__offset - self.__position) % Rotor.__max_position
    def encode_right(self, pos):
        return self.__encode(pos, self.__right_to_left)
    def encode_left(self, pos):
        return self.__encode(pos, self.__left_to_right)
    @staticproperty
    def RotorTypeI(self):
        return Rotor('QRSTUVWXYZABCDEFGHIJKLMNOP', 'XUSPAIBRCJEKMFLGDQVZNTOWYH')
    @staticproperty
    def RotorTypeII(self):
        return Rotor('EFGHIJKLMNOPQRSTUVWXYZABCD', 'SIRUXBLHWTMCQGZNPYFVOEAJDK')
    @staticproperty
    def RotorTypeIII(self):
        return Rotor('VWXYZABCDEFGHIJKLMNOPQRSTU', 'MUSQOBDFHJLCPRTXVZNYEIWGAK')
    @staticproperty
    def ReflectorB(self):
        return Rotor('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
    @staticproperty
    def ReflectorC(self):
        return Rotor('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')