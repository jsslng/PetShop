# -*- coding: utf-8 -*-


class Animal:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
    def __str__(self):
        return "Animal: %s, %d, %s" %(self.nome, self.idade, self. raca)

class Cachorro(Animal):
    def agir(self):
        print "WOOF! WOOF!"

class Gato(Animal):
    def agir(self):
        print "MEOW... MEOW..."
class Passaro(Animal):
    def agir(self):
        print "~~singing bird~~"

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



