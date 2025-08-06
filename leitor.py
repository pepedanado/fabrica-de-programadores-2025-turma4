import csv
nome_do_arquivo = 'OCORRENCIAS_2025.csv'
Carabina_Fuzil = 0
Espingarda = 0
Fuzil = 0
Garrucha = 0
Garruchao = 0
Pistola = 0
Pistolao = 0
Revolver = 0
Rifle = 0
try:
    exemplo_arquivo = open(nome_do_arquivo)
    exemplo_leitor = csv.reader(exemplo_arquivo,
                                delimiter=';',
                                dialect='excel')
    for linha in exemplo_leitor:
        '''print('Linha #%s <%s>'
        % (exemplo_leitor.leitor.line_num, linha))'''
        if linha[4].strip(" ") == "Carabina/Fuzil":
            Carabina_Fuzil += 1
        
        elif linha[4].strip(" ") == "Espingarda":
            Espingarda += 1

        elif linha[4].strip(" ") == "Fuzil":
            Fuzil += 1
        
        elif linha[4].strip(" ") == "Garrucha":
            Garrucha += 1

        elif linha[4].strip(" ") == "Garruchao":
            Garruchao += 1

        elif linha[4].strip(" ") == "Gistola":
            Pistola += 1

        elif linha[4].strip(" ") == "Pistolao":
            Pistolao += 1

        elif linha[4].strip(" ") == "Revolver":
            Revolver += 1

        elif linha[4].strip(" ") == "Rifle":
            Rifle += 1
    print(Carabina_Fuzil, Espingarda, Fuzil, Garrucha, Garruchao, Pistola, Pistolao, Revolver, Rifle)
    exemplo_arquivo.close()

except FileNotFoundError:
    print('Arquivo não encontrado')