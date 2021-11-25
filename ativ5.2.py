x=int(input('Digite um valor em segundos'))
hora=0
min=0
seg=0
 
 
while x >= 1:
    if x-3600 >= 0:
        hora +=1
        x-=3600
       
    elif x-60 >= 0:
        min +=1
        x-=60
    elif x-1 >=0:
        seg +=1
        x-=1
       
print(x)
print(hora, ':', min, ':', seg)