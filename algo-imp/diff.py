# Forward Mode Automatic Differentiation (Slope Algorithm) [https://www.youtube.com/watch?v=QwFLA5TrviI]

class Dual:
    def __init__(self, real, dual):
        # Real + dual epsilon
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if isinstance(other, Dual):
            real = self.real + other.real
            dual = self.dual + other.dual
            return Dual(real, dual)

        return Dual(self.real + other, self.dual)
    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, Dual):
            real = self.real * other.real
            # Note: epsilon * epsilon = 0
            dual = self.real * other.dual + self.dual * other.real
            return Dual(real, dual)

        return Dual(self.real * other, self.dual * other)
    __rmul__ = __mul__

def diff(f, x):
    return f(Dual(x, 1)).dual
