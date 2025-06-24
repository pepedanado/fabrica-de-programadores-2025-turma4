import sys
import os


print("Número de parâmetros: %d" % len(sys.argv))
for n,p in enumerate(sys.argv):
    print("Parâmetro %d = %s" % (n,p))
    try:
        os.mkdir(p)
        print(f"""\033[0;32m Pasta '{p}'
        criada com sucesso! ;D""")
    except FileNotFoundError:
        print(f"""\033[0;33m Pasta '{p}'
        não é possível criar... @_@""")
    except OSError:
        print(f"""\033[0;34m '{p}'
        é um arquivo, não uma pasta!!! +_+""")
