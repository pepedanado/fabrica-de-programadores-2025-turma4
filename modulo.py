import random
import math 

numero_aleatorio = random.random()
print(numero_aleatorio)


numero_aleatorio = random.randint(0,10)
print(numero_aleatorio)

brasileirao = ['santos', 'gremio', 'inter', 'corinthians', 'palmeiras', 'sao paulo', 'sport', 'ceara', 'fortaleza', 'flamengo', 'fluminense', 'botafogo', 'vasco', 'bahia']
print(random.choice(brasileirao), " x ", random.choice(brasileirao))

def banco():
    saldo = int(input("digite o saldo bancario: "))
    saque = int(input("digite o valor de saque: "))

    if saldo >= saque:
        saldo = saldo - saque
        print("voce realizou um saque com sucesso")

    else:
        print("voce nao possui saldo suficiente para realizar essa operaçao")


def media_aluno():
    nota1 = int(input("digite a primeira nota: "))
    nota2 = int(input("digite a segunda nota: "))
    media = (nota1+nota2)/2
    if media >= 6:
        print("aprovado")
    else:
        print("reprovado")


def valor():
    valor_parte = float(input("Insira o valor parte: "))
    porcentagem = float(input("Insira o valor da porcentagem: "))
    valor_total = valor_parte * (porcentagem/100)
    print(valor_total)

    if valor_total <= 0.0:
        print("Insira um numero maior que 0")


def mini_equaçao():
    a = float(input("digite o a: "))
    b = float(input("digite o b: "))
    c = float(input("digite o c: "))
    delta = (b**2)-(4*a*c)
    print(delta)
    
    if delta <= 0:
        print("Não tem resoluçao")
    
    else:
        raizquadrada = math.sqrt(delta)
        print(raizquadrada)
        raiz1 = (-b)+(raizquadrada)/2
        raiz2 = (-b)-(raizquadrada)/2
        print("Raiz1:", raiz1,"Raiz2:", raiz2)
mini_equaçao()


def dieta():
    alimentos = int(input("Digite Kg: "))
    gramas = 1000*alimentos
    print(gramas, "g")
    consumo = 50 
    pessoa = gramas/consumo
    print(pessoa, "dias")
dieta()


def função():
    angulo1 = float(input("Digite o primeiro angulo: "))
    angulo2 = float(input("Digite o segundo angulo: "))
    angulo3 = (angulo1**2)+(angulo2**2)  
    resultado = math.sqrt(angulo3)
    print(resultado)
função()


def salario_a_receber():
    horas_trabalhadas = int(input("Horas trabalhadas: "))
    valor_por_hora = int(input("Valor por hora: "))
    desconto = int(input("Desconto: "))
    descendentes = int(input("Numero de descedentes: "))
    salario = horas_trabalhadas*valor_por_hora
    salario_liquido = salario-desconto
    salario_liquido = salario_liquido+(descendentes*100)
    print(salario_liquido)
salario_a_receber()





    












