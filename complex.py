#Shady Salaheldin

class complex:
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return complex(self.real + other, self.img)
        elif isinstance(other, complex):
            return complex(self.real + other.real, self.img + other.img)
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return complex(self.real / other, self.img / other)
        elif isinstance(other, complex):
            return complex(((self.real * other.real) - (self.img * -1 *other.img)) / ((other.real * other.real) +(other.img * other.img)) , (self.real * ( -1 * other.img) + (self.img * other.real))/((other.real * other.real) +(other.img * other.img)))
        else:
            raise TypeError


    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return complex(self.real * other, self.img * other)
        elif isinstance(other, complex):
            return complex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)
        else:
            raise TypeError

    def __radd__(self, other):
        return complex( other + self.real, self.img)

    def __rtruediv__(self, other):
        return complex( (other * self.real) / ((self.real * self.real) +(self.img * self.img)) , (-1 * other * self.img) / ((self.real * self.real) +(self.img * self.img)) )

    def __rmul__(self, other):
        return complex( other * self.real, other * self.img)

    def __rsub__(self, other):
        return complex( other - self.real, (-1) * self.img)

    def __str__(self):
        if (self.real == 0):
            if (self.img == 0):
                return str(0)
            else:
                return str(self.img) + "i"
        if  (self.img == 0):
            return str(self.real)
        if (self.img < 0):
            myimg = -1 * self.img       
            return "(" + str(self.real) + " - " + str(myimg) + "i" + ")"
        else:
            return "(" + str(self.real) + " + " + str(self.img) + "i" + ")"
		

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int) :
            return complex(self.real - other, self.img)
        elif isinstance(other, complex):
            return complex(self.real - other.real , self.img - other.img)
        else:
            raise TypeError

if __name__ == '__main__':

    a = complex(1, 2)
    b = complex(2, 3)

    i = 5

    print('%s + %s = %s' % (a, b, a + b))
    print('%s - %s = %s' % (a, b, a - b))
    print('%s * %s = %s' % (a, b, a * b))
    print('%s / %s = %s' % (a, b, a / b))

    print('%s + %i = %s' % (a, i, a + i))
    print('%s - %i = %s' % (a, i, a - i))
    print('%s * %i = %s' % (a, i, a * i))
    print('%s / %i = %s' % (a, i, a / i))

    print('%i + %s = %s' % (i, a, i + a))
    print('%i - %s = %s' % (i, a, i - a))
    print('%i * %s = %s' % (i, a, i * a))
    print('%i / %s = %s' % (i, a, i / a))
