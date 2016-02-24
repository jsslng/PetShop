# -*- coding: utf-8 -*-


from animal import Animal


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

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def __str__(self):
        return "Cliente %s (%s): %s" % (self.nome, self.email, self.telefone)


class Doutor(Usuario):
    def __init__(self, nome, email, telefone):
        Usuario.__init__(self, nome, email, telefone)
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def __str__(self):
        return "Doutor %s (%s): %s" % (self.nome, self.email, self.telefone)


class Funcionario(Usuario):
    def __init__(self, nome, email, telefone):
        Usuario.__init__(self, nome, email, telefone)
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def __str__(self):
        return "Funcionario %s (%s): %s" % (self.nome, self.email, self.telefone)


def test_usuario():
    usuario = Usuario("Icaro", "icaro@aeroli.to", "51 81963836")
    print usuario
    cliente = Cliente("Igor", "igor@aeroli.to", "51 82399192")
    print cliente

    print cliente.animais
    cliente.adicionar_animal(Animal("fred", 1, "vira-lata"))
    print cliente

    doutor = Doutor("Doctor", "dr@dr.com", "51 2838282")
    print doutor
