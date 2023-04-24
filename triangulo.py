from ponto import Ponto as Po
from math import sqrt

class Triangulo:
    def __init__(self, ponto1, ponto2, ponto3):
        self.p1 = ponto1
        self.p2 = ponto2
        self.p3 = ponto3

    @staticmethod
    def calc_lado(A, B):
        return Po.calc_dist_entre_pontos(A, B)
    
    def calc_area(self):
        L1 = Po.calc_dist_entre_pontos(self.p1, self.p2)
        L2 = Po.calc_dist_entre_pontos(self.p2, self.p3)
        L3 = Po.calc_dist_entre_pontos(self.p3, self.p1)

        semip = (L1 + L2 + L3)/2

        area = sqrt(semip*(semip - L1)*(semip - L2)*(semip - L3))

        return area
    
    def verificar(self):
        L1 = Po.calc_dist_entre_pontos(self.p1, self.p2)
        L2 = Po.calc_dist_entre_pontos(self.p2, self.p3)
        L3 = Po.calc_dist_entre_pontos(self.p3, self.p1)

        if (L1 == L2) and (L1 == L3) :
            return 'Equilatero'
        elif (L1 == L2) or (L1 == L3) or (L2 == L3):
            return 'Isósceles'
        else:
            return 'Escaleno'