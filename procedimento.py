from datetime import date
from usuario import *


class Procedimento():
    def __init__(self, data, nome, custo):
        self.data = data
        self.nome = nome
        self.custo = custo
    def __str__(self):
        return "Data: %s, Nome do procedimento: %s, Custo: %dR$ " %(self.data, self.nome, self.custo)


class Banho(Procedimento):
    def __init__(self, data, nome, custo):
        Procedimento.__init__(self, data, nome, custo)
        self.funcionario = Funcionario(data, nome, custo)


class Cirurgia(Procedimento):
    def __init__(self, data, nome, custo):
        Procedimento.__init__(self, data, nome, custo)
        self.doutor = Doutor(data, nome, custo)


def test_procedimento():
    proc = Banho(str(date.today()), "Cirurgia", 450.00)
    print proc