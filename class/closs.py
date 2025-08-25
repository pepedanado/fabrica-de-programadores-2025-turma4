class Passaro():
    
    def __init__(self, tamanho, cores, espécie, sexo):
        self.tamanho = tamanho
        self.cores = cores
        self.espécie = espécie
        self.sexo = sexo

    def cantar(self):
        return print(f'Sou um {self.espécie} cantando uma bela canção')
    
    def voar(self):
        return print('Batendo as asas e: voando...')
    
passaro1 = Passaro(0.14, ['Marrom', 'Branco', 'Cinza'], 'Pardal', 'M')
passaro1.cantar()

class animais_marinhos():

    def __init__(self, cores, especie, sexo, nome, alimentaçao):
        self.cores = cores
        self.especie = especie
        self.sexo = sexo
        self.nome = nome
        self.alimentaçao = alimentaçao

    def alimentar(self):
        return print(f"{self.nome} se alimenta muito")
    
    def desovar(self):
        return print(f"{self.nome} reproduz desta maneira")
        
    def dormir(self):
        return print(f"{self.nome} está a dormir.")
    
    def comunicar(self):
        return print(f"{self.nome} emite sons de comunicação.")

    def nadar(self):
        return print(f"{self.nome} está a nadar no oceano.")
    
animal = animais_marinhos(['amarelo', 'preto'], 'tubarão', 'M', 'Ted', ' carnívora e se alimenta de outros animais marinhos')
animal.dormir()
animal.alimentar()
    