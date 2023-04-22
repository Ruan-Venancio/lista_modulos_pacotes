from math import pow, sqrt

class Ponto:
    #método construtor
    def __init__(self, eixo_x, eixo_y):
        self.x = eixo_x
        self.y = eixo_y

    # getters e setters
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, novo_x):
        self._x = novo_x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, novo_y):
        self._y = novo_y

    def get_info(self):

        if self.x > 0 and self.y  > 0:
            return self.x, self.y, 1
        elif self.x < 0 and self.y > 0:
            return self.x, self.y, 2
        elif self.x < 0 and self.y < 0:
            return self.x, self.y, 3
        else:
            return self.x, self.y, 4
    
    #método classe
    @classmethod
    def por_tamanho_e_quadrante(cls, hipotenusa, quadrate):
        cateto = sqrt(pow(hipotenusa, 2)/2)

        if quadrate == 1:
            return cls(cateto,cateto)
        elif quadrate == 2:
            return cls(-cateto,cateto)
        elif quadrate == 3:
            return cls(-cateto,-cateto)
        else:
            return cls(cateto,-cateto)
    
    #método estático
    @staticmethod
    def calc_dist_entre_pontos(self, ponto1, ponto2):
        cateto1 = ponto1.x - ponto2.x
        cateto2 = ponto1.y - ponto2.y

        return sqrt(pow(cateto1, 2) + pow(cateto2, 2))