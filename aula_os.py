
import os
"""os.getcwd()
print(os.getcwd())

os.mkdir("d")
os.mkdir("e")
os.mkdir("f")"""

TEXTO1 = "PARA REMOVER PASTA"
arquivo_path = "f"
try:
    os.rmdir(arquivo_path)
    print(f"""\033[0;32m Pasta '{arquivo_path}'
    removida com sucesso! ;D""")
except FileNotFoundError:
    print(f"""\033[0;33m Pasta '{arquivo_path}'
        não encontrada... @_@""")
except OSError:
    print(f"""\033[0;34m '{arquivo_path}'
    é um arquivo, não uma pasta!!! +_+""")



TEXTO2 = "PARA REMOVER ARQUIVO"
arquivo_path = "texto1"
try:
    os.remove(arquivo_path)
    print(f"""\033[0;32m Pasta '{arquivo_path}'
    removida com sucesso! ;D""")
except FileNotFoundError:
    print(f"""\033[0;33m Pasta '{arquivo_path}'
        não encontrada... @_@""")
except OSError:
    print(f"""\033[0;34m '{arquivo_path}'
    é um arquivo, não uma pasta!!! +_+""")


