"""class A:
    def __init__(self, meu_atributo):
        self.meu_atributo = meu_atributo


class B:
   def __init__(self, _meu_atributo):
        self._meu_atributo = _meu_atributo


class C:
    def __init__(self, __meu_atributo):
        self.__meu_atributo = __meu_atributo

        
        
@property
def idade(self):
    return self._idade

@idade.setter
def idade(self, valor):
    self._idade = valor"""


class Pessoa():
    def __init__(self, nome, idade, altura, peso, profissao, email, telefone, estado_civil, ativo, hobbies):
        self._nome = nome                 
        self._idade = idade               
        self._altura = altura              
        self._peso = peso                  
        self._profissao = profissao                   
        self._email = email               
        self._telefone = telefone         
        self._estado_civil = estado_civil          
        self._ativo = ativo               
        self._hobbies = hobbies           

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor > 0:
            self._idade = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if valor > 0:
            self._peso = valor

    @property
    def profissao(self):
        return self._profissao

    @profissao.setter
    def profissao(self, valor):
        self._profissao = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @property
    def estado_civil(self):
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, valor):
        self._estado_civil = valor

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    @property
    def hobbies(self):
        return self._hobbies

    @hobbies.setter
    def hobbies(self, valor):
        if isinstance(valor, list):
            self._hobbies = valor

    def apresentar(self):
        return print(f"Meu nome é: {self.nome}")
    
    def jogar(self):
        return print(f"Meu sonho é ser {self.profissao}")
    
    def telefonar(self):
        return print(f"{self.telefone} toma! este é meu telefone.")

    def comer(self):
        return print(f"Me alimento bastante, por isso peso {self.peso}")
    
    def comunicar(self):
        return print(f"Esse é meu email: {self.email}, se precisar mandar algum documento.")

pessoas = Pessoa('Pedro', 17, 1.76, 77, 'jogador', '1099169069@aluno.santanadeparnaiba.sp.gov.br', '40028922', 'solteiro', 'ativo','Meu hobbie é jogar tenis')
print(pessoas.nome)
pessoas.apresentar()
pessoas.jogar()
pessoas.telefonar()
pessoas.comer()
pessoas.comunicar()