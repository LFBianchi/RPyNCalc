import math

class Rpn():
    mem = []

    def add(self, n):
        self.mem.insert(0, float(n))

    def delete(self):
        self.mem.pop(0)

    def sum(self, n1):
        n2 = self.mem.pop(0)
        return n1 + n2

    def sub(self, n1):
        n2 = self.mem.pop(0)
        return n1 - n2

    def mul(self, n1):
        n2 = self.mem.pop(0)
        return n1 * n2

    def div(self, n1):
        n2 = self.mem.pop(0)
        return n1 / n2

    def log(self, n1):
        if self.mem:
            n2 = self.mem.pop(0)
            return math.log(n1, n2)
        else:
            return math.log(n1)

    def sqrt(self, n1):
        return n1 ** (0.5)

    def pow(self, n1):
        n2 = self.mem.pop(0)
        return n1 ** n2
