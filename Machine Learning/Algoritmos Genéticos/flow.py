import time 
import random
import numpy as np
from random import sample
from random import randint 

 #função solucao
def makespan(instancia, populacao):
    nM = len(instancia)
    tempo = [0]*nM
    for t in populacao:
        for m in range(nM):
            if tempo[m] < tempo[m-1] and m != 0:
                tempo[m] = tempo[m-1]

            tempo[m] += instancia[m][t-1]

    return tempo[nM-1]

#armazenar em uma lista e retornar
def lerInstancias(files):    
    lista = []
    with open(files) as file:
        for line in file:
            new_list = [int (i) for i in line.split(" ")]
            lista.append(new_list)
    return lista

 #limpando os dados do cabeçalho
def data_header(nm, nt):
    getters = [sample (range(1, nt + 1), nt)
                     for i in range (nm)]
    return getters

#seleção da população
def criarPopulacaoInicial(instancia, tamanho): 
    populacao = []
    for i in tamanho:
        t = makespan(instancia, i) #avalia população e retorna com os tempos
        populacao.append([t,i])
    return populacao


def retornaMelhorSolucao(lista): #ordena e separa metade dos dados, sendo estes os melhores tempos
    new_list = sorted(lista, key=lambda item: item[0])
    return new_list[:50] #considerado 50 em razão de alguns sets conterem apenas 100 valores
    
    
#crossover
def remove_time(melhorSolucao): #retorna a lista sem os tempos
    lista = []
    for i in melhorSolucao:
        lista.append(i[1])
    return lista

#se existirem dados duplicados, a função faz a remoção
def remove(lista): #remove os dados iguais, repitidos
    index = [] 
    recurrent = []
    tam = len(lista)
    for i in range(tam):
        for j in range(tam):
            if lista[i] == lista[j] and i != j and lista[i] not in recurrent:
                recurrent.append(lista[i])
                index.append(i) 
    count = 0
    for i in range(tam): #atualiza a lista para recombinar
        if i+1 not in lista:
            lista[count] = i+1
            count+=1
    
    return lista

def recombinacao(populacaoSelecionada):
    filha = []
    linha = 1
    pais = remove_time(populacaoSelecionada)
    tam = len(pais)

    for i in range(tam):
        tmp = pais[i][:(int(len (pais[0])/2))] + pais[linha][(int(len (pais[0])/2)):len (pais[0])] 
        filha.append(remove(tmp))
        if linha < tam -1:
            linha = linha+1
    return filha

def mutacao(novasSolucoes, populacaoSelecionada, size_line):
    mutacao = 0         #identificador
    id_mut = 0          #marcando lugares que terao que sofrer mutacao
    id_mut2 = 0 
    #mutação das recombinações, com 10% de chances para qualquer valor
    for i in range(len(novasSolucoes)):
        mutacao = randint(0, 10)
        if mutacao == 5:
            id_mut = randint(0, size_line-1)
            id_mut2 = randint(0, size_line-1)

            tmp = novasSolucoes[i][id_mut] #troca uma pela outra
            novasSolucoes[i][id_mut] = novasSolucoes[i][id_mut2]
            novasSolucoes[i][id_mut2] = tmp
    #mutação dos 20 melhores        
    mutacoes = []
    for i in range(50):
        if i > 30: break
        mutacao = randint(0,10)
        id_mut = randint(0, size_line-1)
        id_mut2 = randint(0, size_line-1)
        mutacoes.append(populacaoSelecionada[i])
        
        tmp = mutacoes[-1][id_mut] #troca uma pela outra novamente
        mutacoes[-1][id_mut] = mutacoes[-1][id_mut2]
        mutacoes[-1][id_mut2] = tmp
    return novasSolucoes + populacaoSelecionada[:(50 - len(mutacoes))]

def salvarRelatorio(arq, upper_t, lower_t, high_tp, tp_exec, tp_init_loop):
    print("Filename,", arq.split("/")[1], ",Upper bound(Tailard),", lower_t, ",Lower bound(Taillard),", upper_t, file=fout)
    print("New lower bound,", min(high_tp), file=fout)
    print("New upper bound,", max(high_tp), file=fout)
    print("Mean LB,", round(sum(high_tp) / len(high_tp), 4), file=fout)
    print("lb std,", round(np.std(high_tp), 4), file=fout)
    print("Mean Time(t/s),", round(sum(tp_exec) / len(tp_exec), 4), file=fout)
    print("Total time std(t/s),", round(np.std(tp_exec), 2), file=fout)
    print("Total time(t/s),", round(time.time() - tp_init_loop, 4), file=fout)
    print("\n", file=fout)

tempo_inicial = time.time()
FILE = [
    "path/tai20_5.txt",
    "path/tai20_10.txt",
    "path/tai20_20.txt",
    "path/tai50_5.txt",
    "path/tai50_10.txt",
    "path/tai50_20.txt",
    "path/tai100_5.txt",
    "path/tai100_10.txt",
    "path/tai100_20.txt",  
    "path/tai200_10.txt"]

fout = open("relatorio.csv", "w")
for file in FILE:

    lista = []
    lista = lerInstancias(file)
    
    jobs  = int(lista[0][0])
    MACHINES = int(lista[0][1])
    upper_taillard = int(lista[0][3])
    lower_taillard = int(lista[0][4])
        
    instancia = []
    for i in range(1, MACHINES):
        if i > 0:
            instancia.append(lista[i])

    
    i = 0
    time_exec = []                  #tempo de execução
    best_times = []                 #salva os melhores tempos
    worst_time = []                 #guarda piores tempos
    initial = time.time()
    
    while (i < 10): #executar 10 vezes para cada instancia
        populacao = []
        populacao = data_header(100, jobs)
    
        overtime = False            #estouro no tempo
        lower_time = 99999999        #var dos melhores tempos
        upper_time = 0               #piores tempos
        nThreads = 0                #numero de execuções
        
        while (not overtime): # Critério de tempo excedido  
        
            SET = criarPopulacaoInicial(instancia, populacao)
            high_SET = retornaMelhorSolucao(SET) #recebendo os melhores valores de cada arquivo de entrada
    
            if high_SET[0][0] < lower_time:
                lower_time = high_SET[0][0]  #ultima iteração
    
            novas_solucoes = recombinacao(high_SET)
            populacao = mutacao(novas_solucoes, remove_time(high_SET), jobs)
    
            overtime = (time.time() - initial) > 60.0 #TEMPO TOTAL por execução
            nThreads += 1

            #Se o resultado for 10% inferior ao do algoritmo de Taillard
            if lower_time < (lower_taillard * 0.9):
               break
            
        # salvar os tempos para fazer a média
        time_exec.append(time.time() - initial)
        best_times.append(lower_time)
        worst_time.append(upper_time)
    
        i = i + 1
    
    salvarRelatorio(file, lower_taillard, upper_taillard, best_times, time_exec, initial)
fout.close()

tempo_final = time.time()
tempo_final = (tempo_final-tempo_inicial) #tempo total compilação
print("a compilação durou (t/s):", tempo_final)