import glob

def contador(caracter, lista):
      
  pos = ord(caracter)
  lista[pos] = lista[pos] + 1

glob = glob.glob("/Users/Natalia/Documents/projeto/*.*") #alterar o caminho da pasta dependendo do SO

for arq in glob:   
  arqui = open(arq, "r", encoding="latin-1") # Mudar o encoding dependendo do SO
  print (arq)  
  lista = [0] * 256 # cria uma lista vazia

  x = arqui.read(1)
  while len(x) != 0:

    #print (x)
    contador (x, lista)
    x = arqui.read(1)

  for i in range (0, len(lista)):
            
            if i<32 or i>126:
                  caracter = "<" + str(i) + ">"
            else:
                  caracter=chr(i)
                  
            print (caracter+ " " + str(lista[i]))
        
  
  
  
