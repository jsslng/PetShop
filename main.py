# -*- coding: utf-8 -*-
from animal import Cachorro, Gato, Passaro
from procedimento import *


class Gerenciador():
    def menu(self):
        m = True
        animais = [Cachorro("fred", "2", "dog alemao"), Gato ("pepo", "2", "belga"), Passaro("guto", "7", "papagaio"),
                   Cachorro("bia", "2", "poodle")]
        doutor = Doutor("Julio", "julio@doutor.com", "83876545")
        funcionario = Funcionario ("Guta", "guta@funcionario.com", "82345987")
        while m:
            print "0: sair"
            print "1: Cadastro"
            print "2: Listar os animais cadastrados"
            print "3: Listar consultas cadastradas"
            print "4: Listar cirurgias cadastradas"
            print "5: Listar banhos e/ou tosas cadastradas"
            print "6: Deletar animal do cadastro"
            print "7: Deletar a ultima consulta cadastrada"
            print "8 Deletar a ultima cirurgia cadastrada"
            print "9 Deletar o ultimo banho e/ou tosa cadastrado(os)"

            n = raw_input("Digite a opcao: ")

            if n == "0":
                m = False

            elif n == "1":
                tipo_cadastro = raw_input("Digite 1 para cadastrar um animal no sistema, 2 para marcar uma consulta "
                                          "3 para marcar uma cirurgia e 4 para marcar banho e/ou tosa: ")
                if tipo_cadastro == "1":
                    nome = raw_input("Digite o nome do animal: ")
                    idade = raw_input("Digite a idade do animal: ")
                    raca = raw_input("Digite a raca do animal: ")
                    tipo = raw_input("Digite o tipo do animal: ")

                    if tipo == "cachorro":
                        animal = Cachorro(nome, idade, raca)
                        animais.append(animal)
                    elif tipo == "gato":
                        animal = Gato(nome, idade, raca)
                        animais.append(animal)
                    elif tipo == "passaro":
                        animal = Passaro(nome, idade, raca)
                        animais.append(animal)
                    else:
                        print "tipo invalido"

                elif tipo_cadastro == "2":
                    nome_animal = raw_input("Digite o nome do animal: ")
                    for c in animais:
                        if c.nome == nome_animal:
                            data = raw_input("Digite a data no formato mm-dd-yy ")
                            doutor.marcar_consulta(c, data)
                            print "Consulta marcada com sucesso"

                elif tipo_cadastro == "3":
                    nome_animal = raw_input("Digite o nome do animal: ")
                    data = raw_input("Digite a data no formato mm-dd-yy ")
                    for a in animais:
                        if nome_animal == a.nome:
                            doutor.marcar_cirurgia(a, data)
                            print "Consulta marcada com sucesso"

                elif tipo_cadastro == "4":
                    nome_animal = raw_input("Digite o nome do animal: ")
                    data = raw_input("Digite a data no formato mm-dd-yy ")
                    for a in animais:
                        if nome_animal == a.nome:
                            funcionario.marcar_banho_tosa(a, data)
                            print "Banho e/ou tosa marcados com sucesso"

            elif n == "2":
                if not animais:
                    print "Lista de animais esta vazia"
                else:
                    for c in animais:
                        print c

            elif n == "3":
                for c in doutor.consultas:
                    print c

            elif n == "4":
                for c in doutor.cirurgias:
                    print c

            elif n == "5":
                for c in funcionario.banho_tosas:
                    print c

            elif n == "6":
                animal_del = raw_input("Digite o nome do animal a ser deletado: ")
                encontrou = False
                for c in animais:
                    if animal_del == c.nome:
                        animais.remove(c)
                        encontrou = True
                if not encontrou:
                    print "Animal nao encontrado"

            elif n == "7":
                if not doutor.consultas:
                    print "Lista de consultas vazia."
                else:
                    doutor.consultas.remove(doutor.consultas[-1])
            elif n == "8":
                if not doutor.cirurgias:
                    print "Lista de cirurgias vazia."
                else:
                    doutor.cirurgias.remove(doutor.cirurgias[-1])
            elif n == "9":
                if not funcionario.banho_tosas:
                    print "Lista de banhos e tosas vazia"
                else:
                    funcionario.banho_tosas.remove(funcionario.banho_tosas[-1])




def menu_test():
    menu = Gerenciador()
    menu.menu()


menu_test()
