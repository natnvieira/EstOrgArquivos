#Codigo em teste

import glob

def contador(caracter, lista):
      
  pos = ord(caracter)
  lista[pos] = lista[pos] + 1

glob = glob.glob("/home/gabriel/Imagens/*.*") #alterar o caminho da pasta

for arq in glob:   
  arqui = open(arq, "r")
  print (arq)  
  lista = [0] * 255 # cria uma lista vazia

  x = arqui.read(1)
  while len(x) != 0:

    #print (x)
    contador (x, lista)
    x = arqui.read(1)

  for y in lista:
        
    #print (chr(y)) #chr nao esta funcionando
    print (y)
  
  
