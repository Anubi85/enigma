from ._utility import num2char, char2num

class Enigma():
    __max_plugs = 10
    def __init__(self, *args):
        self.__rotors = args[:-1]
        self.__reflector = args[-1]
        self.__plugs = {}
    def add_plug(self, char1, char2):
        if len(self.__plugs) < 2 * Enigma.__max_plugs and not char1 in self.__plugs and not char2 in self.__plugs:
            self.__plugs[char1.lower()] = char2.lower()
            self.__plugs[char2.lower()] = char1.lower()
            return True
        return False
    def encode(self, string):
        out = ''
        for char in string:
            if char.isalpha():
                char_in = char.lower()
                rotate_next = True
                if char_in in self.__plugs:
                    char_in = self.__plugs[char_in]
                p = char2num(char_in)
                for rotor in self.__rotors:
                    if rotate_next:
                        rotate_next = rotor.advance()
                    p = rotor.encode_right(p)
                p = self.__reflector.encode_right(p)
                for rotor in reversed(self.__rotors):
                    p = rotor.encode_left(p)
                char_out = num2char(p)
                if char_out in self.__plugs:
                    char_out = self.__plugs[char_out]
                if char.isupper():
                    char_out = char_out.upper()
            else:
                char_out = char
            out += char_out
        return out
