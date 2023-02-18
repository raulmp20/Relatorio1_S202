class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor

class Elefante(Animal):

    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self,som):
        self.som = som
        print(self.som)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

nome = input('Entre com o nome: ')
idade = int(input('Entre com a idade: '))
especie = input('Entre com a espécie: ')
cor = input('Entre com a cor: ')
tamanho = input('Entre com o tamanho: ')
som = "fuuuu"

elefante1 = Elefante(nome, idade, especie, cor, som, tamanho)

print(elefante1.emitir_som())

if especie == "Africano" and idade < 10:
    elefante1.mudar_tamanho("pequeno")
    elefante1.trombar("Paaah")
elif especie == "Africano" and idade >= 10:
    elefante1.mudar_tamanho("grande")
    elefante1.trombar("PAHHHHHH")

print("Som do", elefante1.nome, ":", elefante1.som)
print("Tamanho do", elefante1.nome, ":", elefante1.tamanho)
