class Fraction(object):

  def __init__(self, n, d):

    '''
     this function operate initialize and called reduce function
    '''
    self.numerator = n
    self.denominator = d
    Fraction.reduce(self)#call reduce function

  def __str__(self):
    return str(self.numerator) + '/' + str(self.denominator)


  def reduce(self):

    """
    Reduces self to simplest terms. Also removes the signs
    if both numerator and denominator are negative.
    Whole numbers (1, 2, ...) are represented as 1/1, 2/1, 3/1 ...
    Raises exception ValueError if the denominator is 0.
    """
    if self.denominator==0:#if d==0, raise Value Error
      raise ValueError
    def gcd(Num1,Num2):
      '''
      find gcd between Num1 and Num2,
      this function use Euclid's algorithm
      ''' 
      if Num1 < Num2:
        (Num1, Num2) = (Num1, Num2)
      while Num2 != 0:
          (Num1, Num2) = (Num2, Num1 % Num2)
      return Num1
    Num=gcd(self.numerator,self.denominator)#calculate gcd between numerator and denominator

    self.numerator=self.numerator//Num
    self.denominator=self.denominator//Num
    
  def adjust(self, s):
    """Multiplies numerator and denominator by factor."""
    self.denominator=self.denominator*s#Multiplies denominator by factor.
    self.numerator=self.numerator*s#Multiplies numerator by factor.
