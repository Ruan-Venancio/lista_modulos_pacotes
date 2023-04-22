from ponto import Ponto as Po
from math import sqrt

class Triangulo:
    def __init__(self, ponto1, ponto2, ponto3):
        self.po1 = ponto1
        self.po2 = ponto2
        self.po3 = ponto3

    def calc_lado(self, A, B):
        return Po.calc_dist_entre_pontos(A, B)
    
    def calc_area(self):
        lado1 = Po.calc_dist_entre_pontos(self.po1, self.po2)
        lado2 = Po.calc_dist_entre_pontos(self.po2, self.po3)
        lado3 = Po.calc_dist_entre_pontos(self.po3, self.po1)

        semip = (lado1 + lado2 + lado3)/2

        area = sqrt(semip(semip - self.po1)(semip - self.po2)(semip - self.po3))

        return area
    
    def verificar(self):
        lado1 = Po.calc_dist_entre_pontos(self.po1, self.po2)
        lado2 = Po.calc_dist_entre_pontos(self.po2, self.po3)
        lado3 = Po.calc_dist_entre_pontos(self.po3, self.po1)

        if (lado1 == lado2) and (lado1 == lado3) :
            return 'Equilatero'
        elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
            return 'Isósceles'
        else:
            return 'Escaleno'