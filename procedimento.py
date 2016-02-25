# -*- coding: utf-8 -*-


from datetime import date
from usuario import *


class Procedimento:
    def __init__(self, data, nome, custo):
        self.data = data
        self.nome = nome
        self.custo = custo

    def __str__(self):
        return "Data: %s, Nome do procedimento: %s, Custo: %dR$ " % (self.data, self.nome, self.custo)


class Banho(Procedimento):
    def __init__(self, data, nome, custo, funcionario, animal):
        Procedimento.__init__(self, data, nome, custo, id)
        self.funcionario = funcionario
        self.animal = animal

    def __str__(self):
        return "Data: %s, Nome do procedimento: %s, Custo: %dR$, Profissional responsavel: %s " % (self.data, self.nome,
                                                                                                   self.custo, self.funcionario.nome)


class Consulta(Procedimento):
    def __init__(self, data, nome, custo, doutor, animal):
        Procedimento.__init__(self, data, nome, custo)
        self.doutor = doutor
        self.animal = animal

    def __str__(self):
        return "Data: %s, Nome do procedimento: %s, Custo: %sR$, Profissional responsavel: %s " % (self.data, self.nome,
                                                                                                   self.custo, self.doutor.nome)


def test_procedimento():
    doutor = Doutor("Julio", "blablalbablalb", 376538745)
    proc = Banho(str(date.today()), "Cirurgia", 450.00, doutor)
    print proc
