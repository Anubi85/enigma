__version__ = '0.0.1a'
__author__ = 'Andrea Parisotto'

from .enigma import Enigma
from .rotor import Rotor

# Standard rotors
RotorTypeI = Rotor('QRSTUVWXYZABCDEFGHIJKLMNOP', 'XUSPAIBRCJEKMFLGDQVZNTOWYH')
RotorTypeII = Rotor('EFGHIJKLMNOPQRSTUVWXYZABCD', 'SIRUXBLHWTMCQGZNPYFVOEAJDK')
RotorTypeIII = Rotor('VWXYZABCDEFGHIJKLMNOPQRSTU', 'MUSQOBDFHJLCPRTXVZNYEIWGAK')
# Standard reflectors
ReflectorB = Rotor('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
ReflectorC = Rotor('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')