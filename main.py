# -*- coding: utf-8 -*-
from animal import Animal


class Gerenciador():
    def menu(self):
        m = True
        animais = []
        while m:
            print "0: sair"
            print "1: cadastrar um novo animal"
            print "2: listar os animais cadastrados"
            n = raw_input("Digite a opcao: ")

            if n == "0":
                m = False
            elif n == "1":
                nome = raw_input("Digite o nome do animal: ")
                idade = raw_input("Digite a idade do animal: ")
                raca = raw_input("Digite a raca do animal: ")
                animal = Animal(nome, idade, raca)
                animais.append(animal)
            elif n == "2":
                for c in animais:
                    print c


def menu_test():
    menu = Gerenciador()
    menu.menu()


menu_test()
