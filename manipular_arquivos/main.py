#Programa que esrceve em arquivo

#LEMBRAR DE SALVAR O ARQUIVO MAIN ANTES DE RODAR/ COMITAR   

try:
    arquivo = open("dados/dados.txt", "a")
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

    teste = 10+"salve"    #testando o except do erro por divisão por 0

except FileNotFoundError:
    print("Arquivo ou diretório não encontrado")
except ZeroDivisionError:
    print("ta dividindo por 0 doente, faz o limite")
except:
    print("Algo deu bosta mano")
finally:
    print("agora ta suave")