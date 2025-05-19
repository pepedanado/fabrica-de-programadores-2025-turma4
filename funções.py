"""texto_escrito="este livro é legal!"
outro_texto="vou aprender a programar"
outro_texto=texto_escrito
print(outro_texto)
balas_subtraidas=3
quantidade_balas=20
quantidade_balas-=balas_subtraidas
print(quantidade_balas)
nome=input()
saudacao="olá"+nome
print(saudacao)
numero_um=input()
numero_dois=input()
resultado_soma=float(numero_um)+float(numero_dois)
resultado_soma_texto=str(resultado_soma)
mensagem="O resultado da soma é:"+resultado_soma_texto
print(mensagem)
"""
def quadrado(lado):
    area=lado*lado
    return area
#quadrado(int(input()))

def reajuste(salario):
    novo_salario=salario*+15/100
    print(novo_salario)
#reajuste(int(input()))



def triangulo():
    b=input()
    h=input()
    area=(int(b)*int(h))/2
    A=area
    print(A)

#triangulo()

def celsius():
    temperatura=int(input("digite sua temperatura"))
    F=(9*temperatura+160)/5

    print(F)
#celsius()

def novovalor():
    x=int(input("digite o primeiro"))
    y=int(input("digite o segundo"))
    z=(x)
    x=(y)
    y=(z)
    print(x, y)
#novovalor()

def paralelepipedo():
    comprimento=int(input("digite o compr"))
    largura=int(input("digite a lar"))
    altura=int(input("digite a alt"))
    volume=(comprimento*largura*altura)
    print(volume)
#paralelepipedo()

def poupança():
    aplicaçao=int(input("digite o valor da aplicaçao: "))
    valor=(aplicaçao/100*1*1.3)
    print(valor)
#poupança()

def somadosquadrados():
    x=int(input())
    y=int(input())
    quadrado1= quadrado(x)
    quadrado2= quadrado(y)
    print(quadrado1+quadrado2)
#somadosquadrados()

def diferença():
    x=float(input())
    y=float(input())
    numero1= (x)
    numero2= (y)
    print(numero1-numero2)
#diferença()

def idade():
    anodenascimento=int(input("ano de nascimento: "))
    idadefutura=int(input("idade daqui 17 anos: "))
    ano1=(idadefutura-anodenascimento)
    ano2=(idadefutura-anodenascimento)
    print(ano1, ano2+17)
#idade()




    
    





    

   
    
    
    


