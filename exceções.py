
try:
    divisão = 10/0
    print(divisão)
except:
    print('''Não foi possivel realizar essa operação!''')

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Por favor, não utilize zeros!")
    except:
        print("\033[91m Algo deu errado...")
    else:
        print(f"Seu resultado é: {result}")
    finally:
        print("\033[92m Vamos de novo?")
divide("20x","4y")

def programa():
    numero = int(input("digite um numero: "))
    match numero:
        case 1:
            print("positivo")
    
        case 0:
            print("zero")
        case -1:
            print("negativo")
programa()
