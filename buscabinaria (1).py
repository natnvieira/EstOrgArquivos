#!/usr/bin/python3
# Busca (pesquisa) binária

import struct 

#estrutura do arquivo
reg = struct.Struct("72s72s72s72s2s8s2s")

#Abrir o arquivo
try: 
   arquivo = open("cep_ordenado.dat","r",encoding = "latin1")

except:
 	print ("Erro ao abrir o arquivo")

	

cep = input("\nCEP que deseja buscar (insira apenas números)")


#Busca Binária

inicio = 0
arquivo.seek(0,2)
fim = arquivo.tell()
fim2 = fim / reg.size
count = 0

while (inicio <= fim2):
	
	meio = int((inicio+fim2)/2)
	arquivo.seek(meio * reg.size)
	linha = arquivo.read(reg.size)
	count += 1
	if len(linha) < reg.size:
		print ("CEP não localizado")
		break
	dados = reg.unpack(linha.encode("latin1"))
	if dados[5].decode("latin1") == cep:
		print ("Rua: %s" % dados[0].decode("latin1"))
		print ("Bairro: %s" % dados[1].decode("latin1"))
		print ("Cidade: %s" % dados[2].decode("latin1"))
		print ("Estado: %s" % dados[3].decode("latin1"))
		print ("Sigla: %s" % dados[4].decode("latin1"))
		print ("CEP: %s\n\n" % dados[5].decode("latin1"))
		arquivo.close()
		break
	elif dados[5].decode("latin1") > cep :
		fim2 = meio - 1
	else:
		inicio = meio + 1

