
# Implement rational numbers:
# The implementation should include:
#     * initialization
#     * "+, -, *, /"
#     * pretty representation for printing
#     * GCD normalization after each operation

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

class RationalNumber:
    numerator   = 0
    denominator = 1
    
    
    
    def __init__ (self, arg_numerator, arg_denominator):
        self.numerator   = arg_numerator
        if arg_denominator == 0 : raise Exception("Devision by Zero +{}".format(self))
        else : self.denominator = arg_denominator
        self.RationalSimplify()
     
    def RationalSimplify (self):
        r =gcd(self.numerator,self.denominator)
        self.denominator //= r 
        self.numerator   //= r
    
            
    def __add__(self, other):

         numerator    = (self.denominator * other.numerator)+(self.numerator * other.denominator)  
         denominator =   self.denominator*other.denominator
         
         return RationalNumber(numerator,denominator)

    def __sub__(self, other): 
        numerator    = (self.numerator * other.denominator)-(self.denominator * other.numerator)
        denominator  = self.denominator *other.denominator
        
        return RationalNumber(numerator,denominator)

    def __mul__(self, other): 
        denominator = self.denominator*other.denominator
        numerator   = self.numerator*other.numerator
        
        return RationalNumber(numerator,denominator)

    def __truediv__(self, other):
        denominator = self.denominator * other.numerator
        numerator   = self.numerator   * other.denominator
        
        return RationalNumber(numerator,denominator)

    def __str__ (self):
        return "{0} / {1}".format(self.numerator,self.denominator)
    
a = RationalNumber(1,4)
b = RationalNumber(2,3)
print (a+b)
print (b-a)
print (a*b)
print (a/b)

        
        