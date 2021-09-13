
from __future__ import print_function
from random import *
import copy
import time

print("~" * 20)  # separação dos itens para ajudar no desing
print("ALOCAÇÃO DE MEMÓRIA")  # Identificação
print("~" * 20)  # separação dos itens para ajudar no desing
print(
    "Grupo:\nCarlos Henrique,\nJoão Brandão,\nMatheus Leindorf e\nManoel Bina.")  # Integrantes do rupo que realizaram o trabalho
print("~" * 20)  # separação dos itens para ajudar no desing
print(
    "Orienteção sobre o trabalho:""\nDesenvolvemos um software sobre alocação de memória pensando nas pessoas que não tem conhecimento de programação, portanto na hora que digitar a posição das linhas e colunas considere-as começando no 1.")
# Na linha de cima temos as orientações sobre o nosso programa
print("~" * 20)  # separação dos itens para ajudar no desing

linhas = int(input("Digite o numero de linhas:"))  # Espaço onde o usuário coloca o número de linhas da matriz
colunas = int(input("Digite o numero de colunas:"))  # Espaço onde o usuário coloca o número de colunas da matriz

matriz = []  # criamos uma matriz

linhas1 = 1  # Definimos a variavel linha1 começando no 1
while linhas1 <= linhas:
    lista = []  # a cada linha ele vai criar uma lista
    colunas1 = 1 # colunas1 fica com valor igual a um
    while colunas1 <= colunas: # enquanto colunas1 for menor ou igual ao colunas
        lista.append(randint(0, 1))  # a cada coluna ele vai gerar um numero aleatorio entre 0 e 1
        colunas1 += 1 # adicionamos mais um na variavel colunas1
    matriz.append(lista)  # adicionamos a lista dentro da matriz
    linhas1 += 1 # adicionamos mais um na variavel colunas1


def matriz_grafica(): # função para executar a visualização da matriz grafica
    for i in matriz:  # verifica as linhas da matriz
        lista = []  # cria uma lista
        soma_coluna = 0  # atribui a 'soma_coluna' um 0
        for n in i:  # verificação se na matriz tem um '0' ou '1'
            if n == 0 and soma_coluna == colunas - 1:  # verifica se o n tem valor igual a '0'
                lista.append("| |")  # utilizamos esse 'if' caso o valor verificado seja o ultimo da coluna
            elif n == 1 and soma_coluna == colunas - 1:  # verifica se o n tem valor igual a 1
                lista.append("|X|")  # utilizamos esse 'elif' caso o valor verificado seja o ultimo da coluna
            elif n == 0:  # se o n ter valor igual a 0
                lista.append("| ")  # utilizado para separa os itens do meio da matriz
            elif n == 1:  # se n tem valor igual a 1
                lista.append("|X")  # utilizado separa os itens no meio da matriz
            soma_coluna += 1  # serve para identificar qual o ultimo valor da coluna
        print(*lista, sep='')  # utilizado para retirar simbolos como virgulas, aspas e colchetes
        lista.clear()  # serve para esquecer a linha atual e ir para a proxima linha
    menu()  # chama a função menu para realizar outra ação


def first_fit():  # função para executar a 'first fit'
    espaco_requisitado = int(input(
        "Digite o número de espaços que você deseja ocupar:"))  # local onde o usuario coloca o tamanho da alocação
    soma = 0  # definimos a soma começando no 0
    coordenada_linha = 1  # definimos a 'coordenada_linha' com valor 1
    erro = 0  # atribui o valor de 0 para a variavel erro
    lista_de_coordenadas_linhas = []  # cria uma lista apenas com as linhas
    lista_de_coordenadas_colunas = []  # cria outra lista apenas com as colunas
    for linha in matriz:  # vair testar todas as linhas dentro da matriz
        coordenada_coluna = 1  # atribuimos o valor da coluna igual a 1
        for digito in linha:  # testa todos os digitos dentro das linhas
            if erro == 0:  # se o erro for
                if digito == 0:  # se o digito for igual a o
                    soma += 1  # soma o valor que temos (0) com 1 e aparece um "x" mostrando que tem alguma coisa alocado
                    lista_de_coordenadas_linhas.append(
                        coordenada_linha - 1)  # guarda a localização do "0" de cada linha na variavel 'lista_de_coordenadas_linhas'
                    lista_de_coordenadas_colunas.append(
                        coordenada_coluna - 1)  # guarda a localização do "0" de cada coluna na variavel 'lista_de_coordenadas_colunas'
                    if soma == espaco_requisitado:  # Se a soma for igual ao tamanho requisitado pelo usuario
                        erro = 1  # mostra um "x"
                        x = 1  # x tem valor igual a 1
                        y = 0 # y tem valor igual a 0
                        while x <= espaco_requisitado:
                            matriz[lista_de_coordenadas_linhas[y]][lista_de_coordenadas_colunas[
                                y]] = 1  # verificar se na linha e na coluna tem alguma coisa alocada
                            x += 1  # se nao tiver nada ele aloca mudando para 1
                            y += 1  # se nao tiver nada ele aloca mudando para 1
                        matriz_grafica()  # chama a matriz grafica e ja mostra a alocação
                elif digito == 1:  # Se o digito for 1
                    soma = 0  # atribui um 0
                    if soma != espaco_requisitado:  # caso a soma seja diferente do tamanho da alocação solicitada
                        lista_de_coordenadas_linhas.clear()  # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
                        lista_de_coordenadas_colunas.clear()  # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
                        lista_de_coordenadas_linhas = []  # cria nova lista chamada 'lista_de_coordenadas_linhas'
                        lista_de_coordenadas_colunas = []  # cria nova lista chamada 'lista_de_coordenadas_colunas'
            coordenada_coluna += 1  # serve para ir para a proxima coordenada da coluna
        coordenada_linha += 1  # serve para ir para a proxima coordenada da linha
    if erro == 0:  # se o erro for '0'
        print(
            "Não existe espaço o suficiente para o tamanho requisitado.")  # mensagem que é apresentado para o usuario caso nao tenha mais espaço para alocação
        first_fit()  # chama a função para tentar o 'first fit' novamente
    menu()  # chama a função do menu para poder escolher outra opção


def best_fit():  # função para executar o 'best fit'
    espaco_requisitado = int(input(
        "Digite o número de espaços que você deseja ocupar:"))  # espaço para o usuario digitar a quantidade de espaços que ele deseja
    soma = 0  # espaco definido começando em 0
    coordenada_linha = 0  # linha começando em 0 tambem
    erro = 0  # validacao do parametro
    lista_de_coordenadas_linhas = []  # linha a ser gerada
    lista_de_coordenadas_colunas = []  # coluna a ser gerada
    coordenadas_de_cada_soma_linhas = []  # a linha extra para poder gerar um .append
    coordenadas_de_cada_soma_colunas = []  # a coluna extra para poder gerar um .append
    lista_somas = []  # encontra o valor requisitado de melhor espaco conforme o pedido
    for linha in matriz:  # testar as linhas da matriz
        coordenada_coluna = 0  # coluna tem valor 0
        for digito in linha:  # testar os digitos na linha
            if erro == 0:  # parametro que visualiza a matriz e as localizacoes dos espacos disponiveis
                if digito == 0:  # se o digito for igual a 0
                    soma += 1  # ele fica com valor 1
                    lista_de_coordenadas_linhas.append(
                        coordenada_linha)  # adiciona o valor na variavel coordenada_linha
                    lista_de_coordenadas_colunas.append(
                        coordenada_coluna)  # adiciona o valor na variavel coordenada_coluna
                elif digito == 1:  # caso o digito seja igual a 1
                    if soma < espaco_requisitado:  # primeiro parametro que visualiza a matriz pela maquina
                        soma = 0  # soma tem valor 0
                        lista_de_coordenadas_colunas = []  # cria uma lista
                        lista_de_coordenadas_linhas = []  # cria uma lista
                    elif soma > espaco_requisitado:  # se o espaco requisitado for maior que o pedido
                        lista_somas.append(soma)  # adiciona o valor na variavel soma
                        coordenadas_de_cada_soma_linhas.append(
                            lista_de_coordenadas_linhas)  # adiciona o valor na variavel lista_de_coordenadas_colunas
                        coordenadas_de_cada_soma_colunas.append(
                            lista_de_coordenadas_colunas)  # adiciona o valor na variavel lista_de_coordenadas_colunas
                        lista_de_coordenadas_colunas = []  # cria uma lista
                        lista_de_coordenadas_linhas = []  # cria uma lista
                        soma = 0  # soma tem valor 0
                    elif soma == espaco_requisitado:  # se o espaco requisitado foi igual ele ira salvar as matrizes e retonar ao soma maior
                        erro = 1  # erro tem valor 1
                        x = 1  # x tem valor 1
                        y = 0  # y tem valor 0
                        while x <= espaco_requisitado:  # enquanto o numero de espaçor for menor ou igual ao espaço requisitado
                            matriz[lista_de_coordenadas_linhas[y]][lista_de_coordenadas_colunas[
                                y]] = 1  # verificar se na linha e na coluna tem alguma coisa alocada
                            x += 1  # espaços disponiveis
                            y += 1  # buscar as coordenadas do espaço alocado
                        matriz_grafica()  # chama a matriz grafica para visualização
            coordenada_coluna += 1  # coluna fica com valor igual a 1
        coordenada_linha += 1  # linha fica com valor igual a 1

    if soma == espaco_requisitado: # se a soma tiver
        erro = 1 # variavel erro recebe o valor igual a um
        x = 1 # x tem o valor igual a um
        y = 0 # y tem o valor igual a zero
        while x <= espaco_requisitado: # enquanto x for menor ou igual ao espaço requisitado
            matriz[lista_de_coordenadas_linhas[y]][lista_de_coordenadas_colunas[y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
            x += 1 # x tem a adição do valor um
            y += 1 # y tem a adição do valor um
        matriz_grafica() # chama a função matriz grafica para visualização
    elif soma > espaco_requisitado: # se soma for maior que espaço_requisitado
        lista_somas.append(soma) # adiciona o valor na variavel soma
        coordenadas_de_cada_soma_linhas.append(lista_de_coordenadas_linhas) # adiciona o valor na variavel lista_de_coordenadas_linhas
        coordenadas_de_cada_soma_colunas.append(lista_de_coordenadas_colunas) # adiciona o valor na variavel lista_de_coordenadas_colunas

    if erro == 0 and sum(lista_somas) == 0: # se o erro for igual a zero ou a soma da lista seja igual a zero
        print("Não existe espaço o suficiente para o tamanho requisitado.") # mostra essa mensagem para o cliente falando que nao ha tamanho suficiente para alocar
        best_fit() # chama a função para tentar fazer o best fit novamente
    elif erro == 0: # se o erro tiver valor zero
        menor_valor_das_somas = min(lista_somas) # se o menor valor da soma for igual ao minnimo da soma da lista
        z = 0 # z recebe o valor igual a zero
        for i in lista_somas: # testa todos os digitos na variavel soma_lista
            if erro == 0: # se o erro for igual a 0
                if i == menor_valor_das_somas: # se o digito for igual o menor valor das somas
                    erro = 2 # erro recebe valor igual a dois
                else:
                    z += 1 # z recebe a adição do um

    if erro == 2: # se o erro for igual a dois
        x = 1 # x tem valor igual a um
        y = 0 # y tem valor igual a zero
        while x <= espaco_requisitado: # enquanto o x for menor ou igual ao espaço requisitado
            matriz[coordenadas_de_cada_soma_linhas[z][y]][coordenadas_de_cada_soma_colunas[z][y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
            x += 1 # soma mais um na variavel x
            y += 1 # soma mais um na variavel y

        # da linha 181 ate 185 ele apaga todas as listas usadas no código, para que ele possa usa-las outras vezes
        coordenadas_de_cada_soma_linhas.clear()
        lista_de_coordenadas_linhas.clear()
        coordenadas_de_cada_soma_colunas.clear()
        lista_de_coordenadas_colunas.clear()
        lista_somas.clear()
        matriz_grafica() # chama a função matriz grafica para visualização
    menu() # chama a função menu para escolher outra opção


def worst_fit():
    espaco_requisitado = int(input(
        "Digite o número de espaços que você deseja ocupar:"))  # espaço para o cliente digitar o tamanho da alocação 'worst fit'
    soma = 0  # definimos a variavel soma com valor inicial 0
    coordenada_linha = 0  # coordenada_linha começa no '0'
    erro = 0  # erro começa com valor 0
    lista_de_coordenadas_linhas = []  # cria uma nova lista
    lista_de_coordenadas_colunas = []  # cria uma nova lista
    coordenadas_de_cada_soma_linhas = []  # cria uma nova lista
    coordenadas_de_cada_soma_colunas = []  # cria uma nova lista
    lista_somas = []  # cria uma nova lista
    for linha in matriz:  # verifica todas as linha dentro da matriz
        coordenada_coluna = 0  # coluna recebe 0 como valor inicial
        for digito in linha:  # verifica todos os digitos em uma linha
            if erro == 0:  # se o erro for 0
                if digito == 0:  # se o digito for 0
                    soma += 1  # acrescenta 1
                    lista_de_coordenadas_linhas.append(
                        coordenada_linha)  # adiciona o valor de lista_de_coordenadas_linhas na variavel coordenada_linha
                    lista_de_coordenadas_colunas.append(
                        coordenada_coluna)  # adiciona o valor de lista_de_coordenadas_colunas na variavel coordenada_coluna
                elif digito == 1:  # se o digito for 1
                    if soma < espaco_requisitado:  # se a soma for menor do que o tamanho que o cliente deseja
                        soma = 0  # soma tem valor 0
                        lista_de_coordenadas_colunas = []  # cria uma nova lista
                        lista_de_coordenadas_linhas = []  # cria uma nova lista
                    elif soma >= espaco_requisitado:  # se a soma for maior ou igual ao tamanho que o cliente deseja
                        lista_somas.append(soma)  # gera matrizes da soma
                        coordenadas_de_cada_soma_linhas.append(lista_de_coordenadas_linhas)  # gera matrizes da linha
                        coordenadas_de_cada_soma_colunas.append(lista_de_coordenadas_colunas)  # gera matrizes da coluna
                        lista_de_coordenadas_colunas = [] # cria uma lista
                        lista_de_coordenadas_linhas = [] # cria uma lista
                        soma = 0 # soma começa no zero
            coordenada_coluna += 1 # coordenada_coluna tem a adição do valor um
        coordenada_linha += 1 # coordenada_linha tem a adição do valor um
    if soma >= espaco_requisitado: # se a soma for maior ou igual ao espaço requisitado
        lista_somas.append(soma)  # adiciona o valor na variavel soma
        coordenadas_de_cada_soma_linhas.append(
            lista_de_coordenadas_linhas)  # adiciona o valor na variavel lista_de_coordenadas_linhas
        coordenadas_de_cada_soma_colunas.append(
            lista_de_coordenadas_colunas)  # adiciona o valor na variavel lista_de_coordenadas_colunas

    if erro == 0 and sum(lista_somas) == 0:  # caso o erro e a soma for '0'
        print(
            "Não existe espaço o suficiente para o tamanho requisitado.")  # Mensagem que mostra que nao tem espaço suficiente para alocar
        worst_fit()  # chama função para tentar fazer novamente a 'worst fit'
    elif erro == 0:  # se o erro for 0
        maior_valor_das_somas = max(lista_somas)  # vai procurar qual o maior espaço diponivel e alocar
        z = 0  # serve para identificar os valores
        for i in lista_somas:  # verifica todos os digitos da 'linha_somas'
            if erro == 0:  # se o erro for igual a 0
                if i == maior_valor_das_somas:  # se o digito for igual ao maior espaço
                    erro = 2
                else:
                    z += 1  # soma mais um ao z
    if erro == 2:  # se o erro for igual a 2
        x = 1  # x fica com valor 1
        y = 0  # y com valor 0
        while x <= espaco_requisitado:  # enquanto o numero de espaços for menor ou iguao ao espaço requisitado
            matriz[coordenadas_de_cada_soma_linhas[z][y]][coordenadas_de_cada_soma_colunas[z][y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
            x += 1 # é adicionado o valor de um na variavel x
            y += 1 # é adicionado o valor de um na variavel y
        coordenadas_de_cada_soma_linhas.clear()  # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
        lista_de_coordenadas_linhas.clear()  # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
        coordenadas_de_cada_soma_colunas.clear()  # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
        lista_de_coordenadas_colunas.clear()  # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
        lista_somas.clear() # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
        matriz_grafica()  # chama a função para visualizar a matriz de forma grafica
    menu()  # chama a função menu para escolher outra função


def desalocacao(): # função para executar a desalocação
    print("Escolha um valor inicial, e um final para desalocar:") # espaço onde o usuario coloca o valor da desalocação

    for i in matriz:  # verifica as linhas da matriz
        lista = []  # cria uma lista
        soma_coluna = 0  # atribui a 'soma_coluna' um 0
        for n in i:  # verificação se na matriz tem um '0' ou '1'
            if n == 0 and soma_coluna == colunas - 1:  # verifica se o n tem valor igual a '0'
                lista.append("| |")  # utilizamos esse 'if' caso o valor verificado seja o ultimo da coluna
            elif n == 1 and soma_coluna == colunas - 1:  # verifica se o n tem valor igual a 1
                lista.append("|X|")  # utilizamos esse 'elif' caso o valor verificado seja o ultimo da coluna
            elif n == 0:  # se o n ter valor igual a 0
                lista.append("| ")  # utilizado para separa os itens do meio da matriz
            elif n == 1:  # se n tem valor igual a 1
                lista.append("|X")  # utilizado separa os itens no meio da matriz
            soma_coluna += 1  # serve para identificar qual o ultimo valor da coluna
        print(*lista, sep='')  # utilizado para retirar simbolos como virgulas, aspas e colchetes
        lista.clear()  # serve para esquecer a linha atual e ir para a proxima linha

    linha_inical = int(
        input("Digite a linha inicial para desalocar:"))  # local onde o usuário digita a linha inicial para desalocar
    coluna_inicial = int(
        input("Digite a coluna inicial para desalocar:"))  # local onde o usuário digita a coluna inicial para desalocar
    linha_final = int(
        input("Digite a linha final para desalocar:"))  # local onde o usuário digita a linha final para desalocar
    coluna_final = int(
        input("Digite a coluna final para desalocar:"))  # local onde o usuário digita a coluna final para desalocar

    soma_linha = 0  # definimos a variavel 'soma_linha' com valor inicial de 0
    for linha in matriz:  # verifica todas as linhas da matriz
        while soma_linha <= linha_final - 1 and soma_linha >= linha_inical - 1: # enquanto a soma linha for menor igual na linha final e maior ou igual na linha inicial
        #(Na linha de cima tem a subtração de menos um por ser um aplicativo pensado em pessoas que nao tem conhecimento que a contagem das listas começam em 0)
            soma_coluna = 0 # soma coluna começa com valor 0
            for coluna in linha: # verifica as colunas nas linhas
                if linha_inical == linha_final: # se a linha inicial for igual a linha final
                    while soma_coluna >= coluna_inicial and soma_coluna <= coluna_final: # enquanto a soma coluna for maior ou igual a coluna inicial e menor ou igual a coluna final
                        matriz[soma_linha][soma_coluna - 1] = 0 # verificar se na linha e na coluna tem algum espaço para alocar
                        soma_coluna += 1 # adicinamos o valor de 1 na variavel soma coluna
                elif soma_linha == linha_inical - 1: # se a soma_coluna for igual a linha inicial
                    while soma_coluna < colunas and soma_coluna >= coluna_inicial - 1: # enquanto a soma_coluna for menor que a coluna e maior ou igual a coluna inicial
                        #(temos a subtração de 1 pois esse programa é pensado para pessoas que nao tem conhecimento que a soma das listas começam no 0)
                        matriz[soma_linha][soma_coluna] = 0 # verificar se na linha e na coluna tem algum espaço para alocar
                        soma_coluna += 1 # a variavel soma_coluna recebe a adição de um
                elif soma_linha == linha_final - 1: # se a variavel soma_linha for igual a coluna_final
                    # (temos a subtração de 1 pois esse programa é pensado para pessoas que nao tem conhecimento que a soma das listas começam no 0)
                    while soma_coluna <= coluna_final - 1: # se a soma_coluna for menor ou igual coluna_final
                        matriz[soma_linha][soma_coluna] = 0 # verificar se na linha e na coluna tem algum espaço para alocar
                        soma_coluna += 1 # a variavel soma_coluna recebe a adição do valor um
                elif soma_linha > linha_inical - 1 and soma_linha < linha_final - 1: # enquanto a soma_linha for maior do que a linha inicial e menor do que a linha_inicial
                    # (temos a subtração de 1 pois esse programa é pensado para pessoas que nao tem conhecimento que a soma das listas começam no 0)
                    while soma_coluna <= colunas - 1: # enquanto a soma_coluna for menor ou igual a colunas
                        # (temos a subtração de 1 pois esse programa é pensado para pessoas que nao tem conhecimento que a soma das listas começam no 0)
                        matriz[soma_linha][soma_coluna] = 0 # verificar se na linha e na coluna tem algum espaço para alocar
                        soma_coluna += 1 # temos a adição do valor 1 na variavel soma_coluna
                soma_coluna += 1 # temos a adição do valor 1 na variavel soma_coluna
            soma_linha += 1 # temos a adição do valor 1 na variavel soma_coluna
        soma_linha += 1 # temos a adição do valor 1 na variavel soma_coluna

    matriz_grafica()  # chama a função para visualização da matriz grafica
    menu()  # chama a função de menu para escolher outra função


def modo_de_teste(): # função para executar o modo de teste
    matriz_padrao = []  # criamos uma nova matriz

    colunas = 5000  # pre-definido o tamanho da matriz
    linhas = 5000  # pre-definido o tamanho da matriz
    contador_de_linhas = 1 # contador de linha tem valor igual a um
    while contador_de_linhas <= linhas: # enquanto o contador de linhas seja menor ou igual ao nuemr das linhas
        lista = [] # cria uma lista
        contador_de_colunas = 1 # contador de coluna tem valor igual a um
        while contador_de_colunas <= colunas: # enquanto o contador de colunas for menor ou igual ao numero de colunas
            lista.append(randint(0, 1)) # gera numeros aleatorios que variam entre 0 e 1
            contador_de_colunas += 1 # contador de colunas tem adição de um valor igual a um
        matriz_padrao.append(lista) # é adicionado o valor na variavel lista
        contador_de_linhas += 1 # contador de linhas recebe valor igual a um

    matriz_first = copy.deepcopy(matriz_padrao)  # faz cópias da 'matriz_padrao' para copiar todas as linhas correras
    matriz_best = copy.deepcopy(matriz_padrao)  # faz cópias da 'matriz_padrao' para copiar todas as linhas correras
    matriz_worst = copy.deepcopy(matriz_padrao)  # faz cópias da 'matriz_padrao' para copiar todas as linhas correras

    espaco_requisitado = []  # espaços que serao alocados na matriz padrao
    n_de_alocacoes = 0 # numero de alocações começa com valor zero

    while n_de_alocacoes < 1000000:  # numero de alocações para fazer
        espaco_requisitado.append(randint(1, 25000000))  # armazena os espaços requisitados
        n_de_alocacoes += 1 # é somado um valor de mais um na variavel numero de alocações

    n_de_alocacoes = 0 # variavel numero de alocação tem valor inicial igual a zero
    acertos_erros = [] # cria uma lista

    start_time = time.time()  # começar a contar o tempo
    while n_de_alocacoes < 1000000:  # repetir o codigo FIRST FIT a quantidade de vezes que tem dentro do while
        coordenada_linha = 1 # variavel coordenada_linha tem valor igual a um
        erro = 0 # erro tem valor igual a zero
        soma = 0 # soma começa com valor igual a zero
        lista_de_coordenadas_linhas = [] # cria uma lista
        lista_de_coordenadas_colunas = [] # cria uma lista
        for linha in matriz_first: # verifica todas as linhas na matriz responsavel pela first fit
            coordenada_coluna = 1
            for digito in linha: # verifica todos os digitos da linha
                if erro == 0: # se o erro for igual a zero
                    if digito == 0: # se o digito for igual a zero
                        soma += 1 # é adicionado valor de mais um na variavel soma
                        lista_de_coordenadas_linhas.append(coordenada_linha - 1) # é adicionado o valor à variavel coordenada_linha - 1 pois esse é um programa pensado nas pessoas que nao tem conhecimento de programação
                        lista_de_coordenadas_colunas.append(coordenada_coluna - 1) # é adicionado o valor à variavel coordenada_coluna - 1 pois esse é um programa pensado nas pessoas que nao tem conhecimento de programação
                        if soma == espaco_requisitado[n_de_alocacoes]: # se a soma for igual ao espaço requisitado
                            erro = 1 # erro tem valor igual a um
                            x = 1 # x tem valor igual a um
                            y = 0 # y tem valor igual a zero
                            while x <= espaco_requisitado[n_de_alocacoes]: # enquanto o x for menor ou igual ao espaço requisitado
                                matriz_first[lista_de_coordenadas_linhas[y]][lista_de_coordenadas_colunas[y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
                                x += 1 # atribuido a variavel x mais um valor
                                y += 1 # atribuido a variavel y mais um valor
                    elif digito == 1: # se o digito for igual a um
                        soma = 0 # soma começa no 0
                        if soma != espaco_requisitado: # se a soma for diferente do espaço requisitado
                            lista_de_coordenadas_linhas.clear() # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
                            lista_de_coordenadas_colunas.clear() # se encontra um digito "1" antes de dois digitos "0", ele apaga a primeira coordenada do digito "0"
                            lista_de_coordenadas_linhas = [] # é criado uma nova lista
                            lista_de_coordenadas_colunas = [] # é criado uma nova lista
                coordenada_coluna += 1 # é adicionado mais um na variavel coodenada_coluna
            coordenada_linha += 1 # é adicionado mais um na variavel coodenada_linha
        n_de_alocacoes += 1  # numero de alocações é somado com mais um
        if erro == 0:  # se o erro for igual a '0'
            acertos_erros.append("não alocou first")  # aloca a mensagem no caso de uma alocação mal-sucedida
        else:
            acertos_erros.append("alocou first")  # aloca a mensagem no caso de uma alocação bem-sucedida

    alocados = acertos_erros.count("alocou first")  # conta quantas vezes aconteceu uma alocação bem-sucedida
    nao_alocados = acertos_erros.count("não alocou first")  # conta quantas vezes aconteceu uma alocação mal-sucedida
    print(
        f"No first fit, foram alocados {alocados} números, e, {nao_alocados} não foram alocados.")  # mostra o numero de alocações feitas bem-sucedidas, e mal-sucedidas
    print(
        f"Tempo levado para fazer a alocação first fit:{time.time() - start_time:.2f} segundos")  # mostra o tempo que durou a alocação em segundos

    n_de_alocacoes = 0 # numero de alocações começa em zero
    start_time = time.time()  # começa a contar o tempo
    while n_de_alocacoes < 1000000:  # repetir o codigo a quantidade de vezes que tem dentro do while
        soma = 0 # soma com valor 0
        coordenada_linha = 0 # coordenada_linha com valor 0
        erro = 0 # erro tem valor 0
        lista_de_coordenadas_linhas = [] # cria lista
        lista_de_coordenadas_colunas = [] # cria lista
        coordenadas_de_cada_soma_linhas = [] # cria lista
        coordenadas_de_cada_soma_colunas = [] # cria lista
        lista_somas = [] # cria lista
        for linha in matriz_best: # testar as linhas da matriz da best fit
            coordenada_coluna = 0 # coordenada_coluna com valor 0
            for digito in linha: # testa todos os digitos da linha da matriz
                if erro == 0: # se o erro tiver valor 0
                    if digito == 0: # se o digito tiver valor 0
                        soma += 1 # atribui valor 1
                        lista_de_coordenadas_linhas.append(coordenada_linha) # atribui o valor na coordenada_linha
                        lista_de_coordenadas_colunas.append(coordenada_coluna) # atribui o valor na coordenada_coluna
                    elif digito == 1: # se o digito for 1
                        if soma < espaco_requisitado[n_de_alocacoes]: # se a soma for menor que o espaço requisitado
                            soma = 0 # Soma tem valor 0
                            lista_de_coordenadas_colunas = [] # cria uma lista
                            lista_de_coordenadas_linhas = [] # cria uma lista
                        elif soma > espaco_requisitado[n_de_alocacoes]: # se a soma for maior do que o espaço requisitado
                            lista_somas.append(soma) # atribui o valor na variavel soma
                            coordenadas_de_cada_soma_linhas.append(lista_de_coordenadas_linhas) # atribui os valores na variavel lista_de_coordenada_linhas
                            coordenadas_de_cada_soma_colunas.append(lista_de_coordenadas_colunas) # atribui os valores na variavel lista_de_coordenada_colunas
                            lista_de_coordenadas_colunas = [] # cria uma lista
                            lista_de_coordenadas_linhas = [] # cria uma lista
                            soma = 0 # soma tem valor 0
                        elif soma == espaco_requisitado[n_de_alocacoes]: # se a soma tiver valor igual ao do espaço_requisitado
                            erro = 1 # erro tem valor 1
                            x = 1 # x fica com valor igual a 1
                            y = 0 # y fica com valor igual a 0
                            while x <= espaco_requisitado[n_de_alocacoes]: # enquanto x for menor ou igual ao espaço requisitado
                                matriz_best[lista_de_coordenadas_linhas[y]][lista_de_coordenadas_colunas[y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
                                x += 1 # adicionamos mais um no valor ja existente de x
                                y += 1 # adicionamos mais um no valor ja existente de y
                coordenada_coluna += 1 # acrescenta mais 1 na variavel coordenada_coluna
            coordenada_linha += 1 # acrescenta mais 1 na variavel coordenada_linha
        if soma == espaco_requisitado: # se a soma tiver valor igual ao do espaço_requisitado
            erro = 1 # erro tem valor igual a 1
            x = 1 # x fica com valor igual a 1
            y = 0 # y fica com valor igual a 0
            while x <= espaco_requisitado[n_de_alocacoes]: # enquanto o x for menor ou igual ao espaço requisitado
                matriz_best[lista_de_coordenadas_linhas[y]][lista_de_coordenadas_colunas[y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
                x += 1 # adicionamos mais um no valor ja existente de x
                y += 1 # adicionamos mais um no valor ja existente de y
        elif soma > espaco_requisitado[n_de_alocacoes]: # se a soma for maior que o espaço requisitado
            lista_somas.append(soma) # adiciona os valores à variavel soma
            coordenadas_de_cada_soma_linhas.append(lista_de_coordenadas_linhas) # adiciona os valores na variavel lista_de_coordenada_linhas
            coordenadas_de_cada_soma_colunas.append(lista_de_coordenadas_colunas) # adiciona os valores na variavel lista_de_coordenadas_colunas
        if erro == 0 and sum(lista_somas) == 0: # se o erro for 0 e a soma da lista for 0
            x = 1 # x tem valor 1
        elif erro == 0: # se o erro for igual a 0
            erro = 1 # erro fica com valor 1
            menor_valor_das_somas = min(lista_somas) # se o menor valor das somas for igual ao menor valor da lista
            z = 0 # z fica com valor igual a 0
            for i in lista_somas: # testa todos os digitos na lista
                if erro == 0: # se o erro for igual a 0
                    if i == menor_valor_das_somas: # se o digito for igual ao menor valor das somas
                        erro = 2 # erro tem valor igual a 2
                    else:
                        z += 1 # atribuimos mais um no z
        if erro == 2: # se o erro for igual a 2
            x = 1 # x fica com valor igual a 1
            y = 0 # y fica com valor igual a 0
            while x <= espaco_requisitado[n_de_alocacoes]: # enquanto o x for menor ou igual ao espaço requisitado
                matriz_best[coordenadas_de_cada_soma_linhas[z][y]][coordenadas_de_cada_soma_colunas[z][y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
                x += 1 # é acrescentado mais um na variavel x
                y += 1 # é acrescentado  mais um na variavel y
        if erro == 0:  # se o erro for 0
            acertos_erros.append("não a locou best")  # aloca a mensagem no caso de uma alocação mal-sucedida
        else:
            acertos_erros.append("alocou best")  # aloca a mensagem no caso de uma alocação bem-sucedida
        n_de_alocacoes += 1 # é adicionado o valor de mais um na variavel de numeros de alocação

    alocados = acertos_erros.count("alocou best")  # conta quantas vezes aconteceu uma alocação bem-sucedida
    nao_alocados = acertos_erros.count("não alocou best")  # conta quantas vezes aconteceu uma alocação mal-sucedida
    print(
        f"No best fit, foram alocados {alocados} números, e, {nao_alocados} não foram alocados.")  # mostra o numero de alocações feitas bem-sucedidas, e mal-sucedidas
    print(
        f"Tempo levado para fazer a alocação best fit:{time.time() - start_time:.2f} segundos")  # mostra o tempo que durou a alocação em segundos

    start_time = time.time()  # começa a contar o tempo
    n_de_alocacoes = 0 # numero de alocações começa no 0
    while n_de_alocacoes < 1000000:  # repete o codigo do tamanho que esta no while
        soma = 0 # soma tem valor 0
        coordenada_linha = 0 # coordenada_linha tem valor 0
        erro = 0 # erro tem valor 0
        lista_de_coordenadas_linhas = [] # criar lista
        lista_de_coordenadas_colunas = [] # criar lista
        coordenadas_de_cada_soma_linhas = [] # criar lista
        coordenadas_de_cada_soma_colunas = [] # criar lista
        lista_somas = [] # criar lista
        for linha in matriz_worst:  # testa as linhas da matriz
            coordenada_coluna = 0 # coordenada_coluna tem valor 0
            for digito in linha:  # testa os digitos da matriz
                if erro == 0:  # se o erro for 0
                    if digito == 0:  # se o erro for 0
                        soma += 1  # Atribui 1
                        lista_de_coordenadas_linhas.append(
                            coordenada_linha)  # adiciona o valor na variavel coordenada_linha
                        lista_de_coordenadas_colunas.append(
                            coordenada_coluna)  # adiciona o valor na variavel coordenada_coluna
                    elif digito == 1:  # se o digito for 1
                        if soma < espaco_requisitado[n_de_alocacoes]:  # se a soma for menor do que o espaço requisitado
                            soma = 0  # soma tem valor 0
                            lista_de_coordenadas_colunas = []  # cria uma matriz lista_de_coordenadas_colunas
                            lista_de_coordenadas_linhas = []  # cria uma matriz lista_de_coordenadas_linhas
                        elif soma >= espaco_requisitado[n_de_alocacoes]:  # se a soma for maior ou igual ao espaço requisitado
                            lista_somas.append(soma)  # adiciona o valor à variavel soma
                            coordenadas_de_cada_soma_linhas.append(
                                lista_de_coordenadas_linhas)  # adiciona o valor para a variavel lista_de_coordenadas_linhas
                            coordenadas_de_cada_soma_colunas.append(
                                lista_de_coordenadas_colunas)  # adiciona o valor na variavel lista_de_coordenadas_colunas
                            lista_de_coordenadas_colunas = []  # cria uma lista chamada lista_de_coordenadas_colunas
                            lista_de_coordenadas_linhas = []  # cria uma lista chamada lista_de_coordenadas_linhas
                            soma = 0  # soma tem valor 0
                coordenada_coluna += 1 # coordenada_coluna fica com valor 1
            coordenada_linha += 1 # a coordenada_linha fica com valor 1
        if soma >= espaco_requisitado[n_de_alocacoes]:  # se a soma for maior ou igual ao espaço requisitado
            lista_somas.append(soma)  # adiciona o valor na variavel soma
            coordenadas_de_cada_soma_linhas.append(
                lista_de_coordenadas_linhas)  # adiciona o valor na variavel lista_de_coordenadas_linhas
            coordenadas_de_cada_soma_colunas.append(
                lista_de_coordenadas_colunas)  # adiciona o valor na variavel lista_de_coordenadas_colunas

        if erro == 0 and sum(lista_somas) == 0:
            acertos_erros.append("não alocou worst")  # mostra os valores que nao foram alocados
        elif erro == 0: # se o erro tiver valor igual a zero
            maior_valor_das_somas = max(lista_somas) # se o maior valor nas somas tiver valor igual ao maximo da lista
            z = 0 # z tem valor igual a 0
            for i in lista_somas: # testa todos os digitos na lista
                if erro == 0: # se o erro tiver valor igual a 0
                    if i == maior_valor_das_somas: # se o digito tiver o mesmo valor do maior valor das somas
                        erro = 2 # erro tem valor igual a 2
                    else:
                        z += 1 # adicionamos mais um no valor ja existente de z
                elif erro == 2: # se o erro tiver valor igual a dois
                    x = 1 # x tem valor igual a um
                    y = 0 # y tem val igual a 0
                    while x <= espaco_requisitado[n_de_alocacoes]: # enquanto x for menor ou igual ao espaço requisitado
                        matriz_worst[coordenadas_de_cada_soma_linhas[z][y]][coordenadas_de_cada_soma_colunas[z][y]] = 1 # verificar se na linha e na coluna tem alguma coisa alocada
                        x += 1 # adicionamos mais um no valor ja existente de x
                        y += 1 # adicionamos mais um no valor ja existente de y
        if erro != 0: # se o erro for diferente de 0
            acertos_erros.append("alocou worst")  # aloca a mensagem no caso de uma alocação bem-sucedida
        n_de_alocacoes += 1 # é adicionado mais um na variavel de numeros de alocação

    alocados = acertos_erros.count("alocou worst")  # conta quantas vezes aconteceu uma alocação bem-sucedida
    nao_alocados = acertos_erros.count("não alocou worst")  # conta quantas vezes aconteceu uma alocação mal-sucedida
    print(
        f"No worst fit, foram alocados {alocados} números, e, {nao_alocados} não foram alocados.")  # mostra o numero de alocações feitas bem-sucedidas, e mal-sucedidas
    print(
        f"Tempo levado para fazer a alocação worst fit:{time.time() - start_time:.2f} segundos")  # Mostra o tempo que durou para alocar


def menu():  # função com as opções disponíveis
    print(
        "\nPara vizualizar a matriz de forma gráfica, digite 1" "\nPara fazer uma alocação first fit, digite 2" "\nPara fazer uma alocação best fit, digite 3" "\nPara fazer uma alocação worst fit, digite 4" "\nPara fazer uma desalocação, digite 5" "\nPara acessar o modo de teste, digite 6")
    # opções disponíveis para o usuário
    digito = int(input("\nDigite a ação que deseja:"))  # espaço para o usuario digitar a opção que deseja
    if digito == 1:  # se o usuario digitar 1
        matriz_grafica()  # a função para visualizar a matriz de forma gráfica é chamada
    elif digito == 2:  # se o usuário digitar 2
        first_fit()  # a função de alocação 'first fit' é chamada
    elif digito == 3:  # se o usuário digitar 3
        best_fit()  # a função de alocação 'best fit' é chamada
    elif digito == 4:  # se o usiário digitar 4
        worst_fit()  # a função de alocação 'worst fit' é chamada
    elif digito == 5:  # se o usuário digitar 5
        desalocacao()  # a função de desalocação é chamada
    elif digito == 6:  # se o usuário digitar 6
        modo_de_teste()  # a função do modo de teste é chamada
    else:
        print(
            "\nSem ação correspondente.")  # caso o usuário digite alguma opção que nao tenha no menu, o sistema retorna essa mensagem de erro
        menu()  # a função menu é chamada para escolher uma outra função


menu()  # função para executar o menu