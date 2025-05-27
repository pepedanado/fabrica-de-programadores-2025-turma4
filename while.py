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