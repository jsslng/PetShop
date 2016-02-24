# -*- coding: utf-8 -*-


class Animal:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    # TODO: definir a funcao `agir` na classe pai pra poder sobrescrever nas filhos

    def __str__(self):
        return "Animal: %s, %d, %s" % (self.nome, self.idade, self.raca)


class Cachorro(Animal):
    def agir(self):
        print "WOOF! WOOF!"

        # TODO: sobrescrever o `__str__`


class Gato(Animal):
    def agir(self):
        print "MEOW... MEOW..."

        # TODO: sobrescrever o `__str__`


class Passaro(Animal):
    def agir(self):
        print "~~singing bird~~"

        # TODO: sobrescrever o `__str__`


def test_animal():
    animal = Animal("Fred", 1, "Vira Lata")
    print animal


def test_cachorro():
    cachorro = Cachorro("Bob", 3, "Pastor Alemao")
    cachorro.agir()


def test_gato():
    gato = Gato("Jubs", 2, "Belga")
    gato.agir()


def test_passaro():
    passaro = Passaro("Petter", 5, "Papagaio")
    passaro.agir()
