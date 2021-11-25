x=str(input('Digite uma frase: \n'))
 
aux=x.split()
 
for i in aux:
    t=i.islower()
    sub=str(i)
    if t == False:
        imp=x.replace(sub, '*****')
print(imp)