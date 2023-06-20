import math

class CNum():
    def __init__(self, a: float, b: float = 0) -> None:
        self.Re = a
        self.Im = b


    def __add__(self, addend: "CNum") -> "CNum":
        a = self.Re + addend.Re
        b = self.Im + addend.Im

        return CNum(a, b)

    def __sub__(self, subtrahend: "CNum") -> "CNum":
        a = self.Re - subtrahend.Re
        b = self.Im - subtrahend.Im

        return CNum(a, b)

    def __mul__(self, multiplicand: "CNum") -> "CNum":
        a = self.Re * multiplicand.Re - self.Im * multiplicand.Im
        b = self.Re * multiplicand.Im + self.Im * multiplicand.Re

        return CNum(a, b)

    def __truediv__(self, divisor: "CNum") -> "CNum":
        a = (self.Re * divisor.Re + divisor.Im * self.Im) / ((divisor.Im) ** 2 + (divisor.Re) ** 2)
        b = (self.Im * divisor.Re - self.Re * divisor.Im) / ((divisor.Im) ** 2 + (divisor.Re) ** 2)

        return CNum(a, b)

    def mag(self) -> float:
        return math.sqrt((self.Re) ** 2 + (self.Im) ** 2)

    def __repr__(self) -> str:
        if self.Im == 0:
            return f"{self.Re}"
        if self.Re == 0:
            return f"{self.Im}i"
        if self.Im < 0:
            return f"{self.Re} - {abs(self.Im)}i"
        else:
            return f"{self.Re} + {self.Im}i"