#Programa que esrceve em arquivo

#LEMBRAR DE SALVAR O ARQUIVO MAIN ANTES DE RODAR/ COMITAR   

arquivo = open("dados.txt", "w")
continuar = True

while continuar:
    equipe = input("Equipe (vazio para sair):")
    #TODA STRING VAZIA É FALSE
    #portanto entra no if se equipe for vazio
    if not equipe:
        continuar = False
        continue    #continua a execução do loop, testa e controla a variável continue
    arquivo.write(equipe + '\n')
arquivo.close()
