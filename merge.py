#!/usr/bin/python3
#-*- coding: latin1 -*-

import struct
import os

reg = struct.Struct("72s72s72s72s2s8s2s")  #Criacao da estrutura

arq = open("cep.dat","rb")
linha = arq.read(reg.size * 5)
count = 0
while len(linha) != 0:  #Loop para particionar em arquivos menores

    arquivo = "parte%d.dat" % count    
    arq1 = open(arquivo,"wb+")
    arq1.write(linha)
    arq1.seek(0,0)
    linha2 = arq1.read(reg.size)
    lista = list()
	
    while len(linha2) == reg.size:  #Loop para adicionar na lista
            
        dados = reg.unpack(linha2)
        lista.append(dados)
        linha2 = arq1.read(reg.size)

    lista.sort(key=lambda x: x[5])  # Ordenacao das partes
    arq1.seek(0,0)
	
    for x in lista: # Inserindo as tuplas no arquivo
        v1 = x[0]
        v2 = x[1]
        v3 = x[2]
        v4 = x[3]
        v5 = x[4]
        v6 = x[5]
        v7 = x[6]

        pacote = reg.pack(v1,v2,v3,v4,v5,v6,v7)
        arq1.write(pacote)

    arq1.close()
    count = count + 1
    linha = arq.read(reg.size * 5)

#Fechando o arquivo de CEP.dat
arq.close()
