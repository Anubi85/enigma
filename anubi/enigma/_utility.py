__char_num = [('a',0),('b',1),('c',2),('d',3),('e',4),('f',5),('g',6),('h',7),('i',8),('j',9),('k',10),('l',11),('m',12),('n',13),('o',14),('p',15),('q',16),('r',17),('s',18),('t',19),('u',20),('v',21),('w',22),('x',23),('y',24),('z',25)]

def char2num(char):
    return next(filter(lambda x: x[0] == char.lower(), __char_num))[1]

def num2char(num):
    return next(filter(lambda x: x[1] == num, __char_num))[0]

class __staticproperty_descriptor():
    def __init__(self, get):
        self.__get = get
    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        return self.__get.__get__(obj, cls)()

def staticproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return __staticproperty_descriptor(func)