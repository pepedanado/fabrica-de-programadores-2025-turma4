import statistics

x = 1
while x<=100:
    print(x)
    x = x+1

x = 50
while 50<=x<=100:
    print(x)
    x = x+1

x = 10
while 0<=x<=10:
    print(x)
    x = x-1
print("Fogo!")

fim = int(input("Digite o úlimo numero a imprimir:"))
x = 0
while x<=fim:
    if x %2 == 0:
        print(x)
    x = x+1

fim = int(input("Digite o úlimo numero a imprimir:"))
x = 0
while x<=fim:
    if x %2 == 1:
        print(x)
    x = x+1

n = int(input("tabuada de:"))
x = 1
while x<=100:
    print(n*x)
    x=x+1

n = int(input("tabuada de: "))
y = 1
conta = n 
while y<=10:
    print(conta, "x" ,y ,"=", n*y)
    y=y+1

n = int(input("tabuada de: "))
y = int(input("valor y, inicio da tabuada: "))
z = int(input("fim da tabuada: "))
conta = n 
while y<=z:
    print(conta, "x" ,y ,"=", n*y)
    y=y+1

s = 0
while True:
    v = int(input("Digite um numero a somar ou 0 para sair: "))
    if v==0:
        break
    s = s+v
print(s)

lista = []
while True:
    n = int(input("Digite um numero: "))
    if n==0:
        break
    lista.append(n)

x = 0
while x < len(lista):
    print(lista[x])
    x=x+1
media = statistics.mean(lista)
print("media:", media)

L=[8,9,15]
for e in L:
    print(e)

L=['maça', 'peras', 'kiwis']
for s in L:
    for letra in s:
        print(letra)

L=[1,7,2,4]
maximo=L[0]
for e in L:
     if e >maximo:
         maximo = e
print(maximo)

L=[1,7,2,4]
menor=L[0]
for e in L:
     if e < menor:
         menor = e
print(menor)


for v in range(5, 8):
    print(v)

for t in range (3,33,3):
    print(t, end=" ")


