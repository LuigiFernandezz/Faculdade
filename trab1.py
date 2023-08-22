#INTEGRANTES: LUIGI FERNANDES, LUCAS CORREA, ARTHUR PENNA

#abertura do arquivo dump txt
arquivo = open("laco.txt")

#definiçao previa dos clocks de cada instrução dados pelo usuario
print("Organizacao processador A")
U_A = int(input("Ciclos da instrucao U:"))
I_A = int(input("Ciclos da instrucao I:"))
R_A = int(input("Ciclos da instrucao R:"))
S_A = int(input("Ciclos da instrucao S:"))
J_A = int(input("Ciclos da instrucao J:"))
B_A = int(input("Ciclos da instrucao B:"))

tempoA = float(input("Tempo de clock dessa organizacao: "))

print("\n\nOrganizacao processador B")
U_B = int(input("Ciclos da instrucao U:"))
I_B = int(input("Ciclos da instrucao I:"))
R_B = int(input("Ciclos da instrucao R:"))
S_B = int(input("Ciclos da instrucao S:"))
J_B = int(input("Ciclos da instrucao J:"))
B_B = int(input("Ciclos da instrucao B:"))

tempoB = float(input("Tempo de clock dessa organizacao (GHz): "))

#abertura de arquivo

def contagem():
    listaInstrucoes = arquivo.readlines()

    #loop para leitura de cada linha
    instrucoes = []
    for i in range(len(listaInstrucoes)):
        instrucoes.append(listaInstrucoes[i][25:32])  #corte dos 7 últimos digitos e colocar em lista

    #Comparação de cada tipo e adição a uma lista com o numero de ciclos de cada instrucao
    totalA = []
    totalB = []

    for instrucao in instrucoes:
        
        if instrucao == "0010111":
            totalA.append(U_A)
            totalB.append(U_B)
        elif instrucao == "0010011":
            totalA.append(I_A)
            totalB.append(I_B)
        elif instrucao == "0110011":
            totalA.append(R_A)
            totalB.append(R_B)
        elif instrucao == "0100011":
            totalA.append(S_A)
            totalB.append(S_B)
        elif instrucao == "1101111":
            totalA.append(J_A)
            totalB.append(J_B)
        elif instrucao == "1100011":
            totalA.append(B_A)
            totalB.append(B_B)
        else:
            continue

    #Contagem do total de ciclos do programa para cada organização
    qtdCiclosA = sum(totalA)
    qtdCiclosB = sum(totalB)

    print("\nTotal ciclos A:", qtdCiclosA)
    print("Total ciclos B:", qtdCiclosB)

    #Cálculo do CPI médio para A e B
    cpiMedioA = qtdCiclosA/len(instrucoes)
    cpiMedioB= qtdCiclosB/len(instrucoes)

    print("\nCiclo medio A:", cpiMedioA)
    print("Ciclo medio B:", cpiMedioB)


    #Cálculo de desempenho    
    tempoExecA = qtdCiclosA*tempoA
    tempoExecB = qtdCiclosB*tempoB
 
    desempenhoA = 1/tempoExecA
    desempenhoB = 1/tempoExecB

    print("\nDesempenho A:", desempenhoA)
    print("Desempenho B:", desempenhoB)
    #Comparacao de desempenho
    if desempenhoA > desempenhoB:
        diferenca = desempenhoA/desempenhoB #quão mais rapido é

        print("Organizacao A é ",diferenca," vezes mais rápida que B")
    elif desempenhoA == desempenhoB:
        print("Ambas as organizacoes tem a mesma velocidade!")
    else:
        diferenca = desempenhoB/desempenhoA 

        print("Organizacao B é ",diferenca," vezes mais rápida que A")


    #fecha o arquivo de texto
    arquivo.close()

#chamada da função
contagem()
