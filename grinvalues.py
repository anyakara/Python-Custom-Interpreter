import grin
class GrinInt(int):
    def __init__(self, value: int):
        """initializes value"""
        self._value = value

    @staticmethod
    def type():
        """returns type"""
        return int

    def value(self):
        """returns value"""
        return self._value

    def __repr__(self):
        """returns representation"""
        return f"GrinInt({self._value})"

    def __add__(self, other):
        """adding grin types"""
        if type(other._value) == int:
            return self._value + other._value
        elif type(other._value) == float:
            return self._value + other._value
        return NotImplemented

    def __sub__(self, other):
        """subtracting grin types"""
        if type(other._value) == int:
            return int(self._value - other._value)
        elif type(other._value) == float:
            return float(self._value - other._value)
        return NotImplemented

    def __mul__(self, other):
        """multiplying grin types"""
        if type(other._value) == int:
            return int(self._value * other._value)
        elif type(other._value) == float:
            return float(self._value * other._value)
        elif type(other._value) == str:
            return self._value * other._value
        return NotImplemented

    def __truediv__(self, other):
        """dividing grin types"""
        if type(other._value) == int:
            return int(self._value // other._value)
        elif type(other._value) == float:
            return float(self._value / other._value)
        return NotImplemented

class GrinFloat(float):
    def __init__(self, value: float):
        """storing values"""
        self._value = value

    @staticmethod
    def type():
        """returning the inherited type"""
        return float

    def value(self):
        """return value"""
        return self._value

    def __repr__(self):
        """return representation"""
        return f"GrinFloat({self._value})"

    def __add__(self, other):
        """adding grin float with similar grin types"""
        if type(other._value) in [int, float]:
            return float(self._value + other._value)
        return NotImplemented

    def __sub__(self, other):
        """subtracting in grin"""
        if type(other._value) in [int, float]:
            return float(self._value - other._value)
        return NotImplemented

    def __mul__(self, other):
        """multiplying in grin"""
        if type(other._value) in [int, float]:
            return float(self._value * other._value)
        return NotImplemented

    def __truediv__(self, other):
        """dividing in grin"""
        if type(other._value) == int:
            return float(self._value / other._value)
        if type(other._value) == float:
            return float(self._value / other._value)
        return NotImplemented

class GrinStr(str):
    def __init__(self, value: str):
        """storing string value"""
        self._value = value

    @staticmethod
    def type():
        """returning string type"""
        return str

    def value(self):
        """returning internal value"""
        return self._value

    def __repr__(self):
        """return a representation if needed"""
        return f"GrinStr({self._value})"

    def __add__(self, other):
        """adding in grin"""
        if type(other._value) == str:
            return self._value + other._value

    def __mul__(self, other):
        """multiplying in grin"""
        if type(other._value) == int:
            return self._value * other._value


__all__ = [GrinInt.__name__,
           GrinFloat.__name__,
           GrinStr.__name__]
