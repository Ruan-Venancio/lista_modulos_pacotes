from ponto import Ponto as Po
from math import sqrt

class Retangulo:
    def __init__(self, ponto1, ponto2, ponto3, ponto4):
        self.po1 = ponto1
        self.po2 = ponto2
        self.po3 = ponto3
        self.po4 = ponto4
    
    def calc_perimetro(self):
        lado1 = Po.calc_dist_entre_pontos(self.po1, self.po2)
        lado2 = Po.calc_dist_entre_pontos(self.po2, self.po3)
        lado3 = Po.calc_dist_entre_pontos(self.po3, self.po4)
        lado4 = Po.calc_dist_entre_pontos(self.po4, self.po1)

        return lado1 + lado2 + lado3 + lado4
    
    def calc_area(self):
        lado1 = Po.calc_dist_entre_pontos(self.po1, self.po2)
        lado2 = Po.calc_dist_entre_pontos(self.po2, self.po3)
        lado3 = Po.calc_dist_entre_pontos(self.po3, self.po4)
        lado4 = Po.calc_dist_entre_pontos(self.po4, self.po1)

        if lado1 >= lado2 and lado1 >= lado3 and lado1 >= lado4:
            base = lado1
            if lado2 == lado1:
                altura = lado3
            elif lado3 == lado1:
                altura = lado2
            else:
                altura = lado2
        elif lado2 >= lado1 and lado2 >= lado3 and lado2 >= lado4:
            base = lado2
            if lado1 == lado2:
                altura = lado3
            elif lado3 == lado2:
                altura = lado1
            else:
                altura = lado1
        elif lado3 >= lado1 and lado3 >= lado2 and lado3 >= lado4:
            base = lado3
            if lado1 == lado3:
                altura = lado2
            elif lado2 == lado3:
                altura = lado1
            else:
                altura = lado1
        else:
            base = lado4
            if lado1 == lado4:
                altura = lado3
            elif lado2 == lado4:
                altura = lado3
            else:
                altura = lado1
        
        return base * altura
        

