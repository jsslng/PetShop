# -*- coding: utf-8 -*-


class Usuario:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return "Usuario %s (%s): %s" % (self.nome, self.email, self.telefone)


class Cliente(Usuario):
    def __init__(self, nome, email, telefone):
        Usuario.__init__(self, nome, email, telefone)
        self.animais = []

    def __str__(self):
        return "Cliente %s (%s): %s" % (self.nome, self.email, self.telefone)


class Doutor(Usuario):
    def __init__(self, nome, email, telefone):
        Usuario.__init__(self, nome, email, telefone)
        self.animais = []
        self.cirurgias = []
        self.consultas = []

    def marcar_consulta(self, animal, data):
        from procedimento import Consulta
        consulta = Consulta(data, "Consulta", "50,00", self, animal)
        self.consultas.append(consulta)

    def marcar_cirurgia(self, animal, data):
        from procedimento import Consulta
        cirurgia = Consulta(data, "Cirurgia", "200,00", self, animal)
        self.cirurgias.append(cirurgia)



    # criar lista com cirurgias no doutor

    def __str__(self):
        return "Doutor %s (%s): %s" % (self.nome, self.email, self.telefone)


class Funcionario(Usuario):
    def __init__(self, nome, email, telefone):
        Usuario.__init__(self, nome, email, telefone)
        self.animais = []
        self.banho_tosas = []

    def marcar_banho_tosa(self, animal, data):
        from procedimento import Banho
        banho_tosa = Banho(data, "Banho e/ou Tosa", "200,00", self, animal)
        self.banho_tosas.append(banho_tosa)

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def __str__(self):
        return "Funcionario %s (%s): %s" % (self.nome, self.email, self.telefone)


def test_usuario():
    pass
