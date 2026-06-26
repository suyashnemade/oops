class Fraction:

    def __init__(self,n, d):
        self.n = n
        self.d = d
    
    def __str__(self,other):
        return f"{self.n}/{self.d}"
    
    def __add__(self, other):
        temp = self.n * other.d + other.n * self.d
        temp2 = self.d * other.d
        return f"{temp}/{temp2}"
    

    def __sub__(self,other):
        temp = self.n * other.d - other.n * self.d
        temp2 = self.d * other.d
        return f"{temp}/{temp2}"


    def __mul__(self,other):
        temp = self.n * other.n
        temp2 = self.d * other.d
        return f"{temp}/{temp2}"


    def __truediv__(self,other):
        temp = self.n * other.d
        temp2 = self.d * other.n
        return f"{temp}/{temp2}"