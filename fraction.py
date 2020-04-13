class Fraction(object):


    def __init__(self, a, b):
        self.numerator = a
        if b != 0:
            self.denominator = b
        elif b == 0:
            raise "division by zero"
        else:
            self.denominator = 1
        #if self.cheak_trimming:
        #print(self)
        self.trimm_fraction()

    def __add__(self, other):
        if other.denominator == self.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        elif other.denominator %  self.denominator == 0 :
            return Fraction((other.denominator / self.denominator) * self.numerator +  other.numerator  , other.denominator)
        elif self.denominator %  other.denominator == 0:
            return Fraction((self.denominator / other.denominator) * other.numerator +  self.numerator  , self.denominator)
        else:
            return Fraction((self.numerator * other.denominator)  + (other.numerator * self.denominator)  ,  self.denominator * other.denominator)
    def __sub__(self, other):
        if other.denominator == self.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator).trimm_fraction()
        elif other.denominator %  self.denominator == 0 :
            return Fraction((other.denominator / self.denominator) * self.numerator -  other.numerator  , other.denominator)
        elif self.denominator %  other.denominator == 0:
            return Fraction((self.denominator / other.denominator) * other.numerator -  self.numerator  , self.denominator)
        else:
            return Fraction((self.numerator * other.denominator)  - (other.numerator * self.denominator)  ,  self.denominator * other.denominator)
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator , self.denominator * other.denominator)
    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator , self.denominator * other.numerator)
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    def cheak_trimming(self):
        if self.denominator % self.numerator == 0 and  self.numerator != 1:
            return True
        elif self.numerator % self.denominator == 0 and self.denominator != 1:
            return True
        elif self.numerator % 10  == 0 and  self.denominator % 10  == 0:
            return True
        else:
            return False
        
    def trimm_fraction(self):
        #print( self.denominator % self.numerator == 0 and  self.numerator != 1)
        #print( self.numerator % self.denominator == 0 and self.denominator != 1)
        #print( self.numerator % 10  == 0 and  self.denominator % 10  == 0)
        if self.denominator % self.numerator == 0 and  self.numerator != 1:
            
            self.denominator =  int(self.denominator // self.numerator)
            self.numerator = 1
        elif self.numerator % self.denominator == 0 and self.denominator != 1:
            self.numerator = int(self.numerator // self.denominator)
            self.denominator = 1
        elif self.numerator % 10  == 0 and  self.denominator % 10  == 0:
            self.numerator = int(self.numerator // 10)
            self.denominator = self.denominator // 10
        else:
            self.numerator = self.numerator
            self.denominator = self.denominator







