from ._utility import num2char, char2num
import abc

class Enigma(metaclass = abc.ABCMeta):
    __max_plugs = 10
    def __init__(self, reflector):
        self._rotors = []
        self._reflector = reflector
        self._plugs = {}
    def add_plug(self, char1, char2):
        if len(self._plugs) < 2 * Enigma.__max_plugs and not char1 in self._plugs and not char2 in self._plugs:
            self._plugs[char1.lower()] = char2.lower()
            self._plugs[char2.lower()] = char1.lower()
            return True
        return False
    def encode(self, string):
        out = ''
        for char in string:
            if char.isalpha():
                char_in = char.lower()
                rotate_next = True
                if char_in in self._plugs:
                    char_in = self._plugs[char_in]
                p = char2num(char_in)
                for rotor in self._rotors:
                    if rotate_next:
                        rotate_next = rotor.advance()
                    p = rotor.encode_right(p)
                p = self._reflector.encode_right(p)
                for rotor in reversed(self._rotors):
                    p = rotor.encode_left(p)
                char_out = num2char(p)
                if char_out in self._plugs:
                    char_out = self._plugs[char_out]
                if char.isupper():
                    char_out = char_out.upper()
            else:
                char_out = char
            out += char_out
        return out

class EnigmaM1(Enigma):
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        super().__init__(reflector)
        self._rotors.extend([rotor1, rotor2, rotor3])
