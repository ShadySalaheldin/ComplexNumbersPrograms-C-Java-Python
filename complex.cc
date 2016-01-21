/*
Shady Salaheldin
*/

#include <iostream>
#include "complex.h"

complex::complex(double real, double img) : real(real), img(img) {}


complex complex::operator+(const complex &o) const {

    return complex(real + o.real, img + o.img);
}

complex complex::operator+(double n) const {

    return complex(real + n, img);
}

complex complex::operator-(const complex &o) const {

    return complex(real - o.real , img - o.img);
}

complex complex::operator-(double n) const {

    return complex(real - n, img);
}

complex complex::operator*(const complex &o) const {

    return complex(real * o.real - img * o.img, real * o.img + img * o.real);
}

complex complex::operator*(double n) const {

    return complex(real * n, img * n);
}
// there is a problem with complex/complex
complex complex::operator/(const complex &o) const {

    //return complex(real * o.real - img * o.img, real * o.img + img * o.real);
    return complex(((real * o.real) - (img * -1 *o.img)) / ((o.real * o.real) +(o.img * o.img)) , (real * ( -1 * o.img) + (img * o.real))/((o.real * o.real) +(o.img * o.img)));
}

complex complex::operator/(double n) const {

    return complex(real / n, img / n);
}

complex operator+(double n, const complex &o) {

    return complex( n + o.real, o.img);
}

complex operator-(double n, const complex &o) {

    return complex( n - o.real, (-1) * o.img);
}

complex operator*(double n, const complex &o) {

    return complex( n * o.real, n * o.img);
}

complex operator/(double n, const complex &o) {

    return complex( (n * o.real) / ((o.real * o.real) +(o.img * o.img)) , (-1 * n * o.img) / ((o.real * o.real) +(o.img * o.img)) );
}

ostream &operator<<(ostream &out, const complex &o) {
    
    if ( o.real == 0){
         if(o.img == 0){
                  out << 0;    
         }
         else{
                  out << o.img << 'i';   
         }
         return out;
    }
    
         
    if ( o.img == 0){
         out << o.real;
         return out;
    } 
         
    if (o.img < 0){
       double myimg = -1 * o.img;
       out << '(' << o.real << " - " << myimg << 'i' << ')';
       
    }
    else{
         out << '(' << o.real << " + " << o.img << 'i' << ')';
    }
             
    return out;
}
