x=float(input('Digite um valor em reais '))
nota100=0
nota50=0
nota10=0
nota1=1
 
while x >= 1:
    if x-100 >= 0:
        nota100 +=1
        x-=100
       
    elif x-50 >= 0:
        nota50 +=1
        x-=50
    elif x-10 >=0:
        nota10 +=1
        x-=10
       
    elif x-1 >=0:
        nota1 +=1
        x-=1
       
print(x)
print('As notas de 100 são:', nota100)
print('As notas de 50 são:', nota50)
print('As notas de 10 são:', nota10)
print('As notas de 1 são:', nota1-1)