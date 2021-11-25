x=int(input('Digite quantos valores deseja armazenar\n'))
i=0
lista=[]
soma=0
while i < x:
    aux=int(input('Digite o valor'))
    lista.append(aux)
    i+=1
    soma+=aux
 
lista.sort()
print(lista)
maior=lista[x-1]
menor=lista[0]
print('Soma: ', soma)
print('Media: ', soma/x)
print('Maior: ', maior)
print('Menor: ', menor)