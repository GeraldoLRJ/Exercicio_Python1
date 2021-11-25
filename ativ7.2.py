x=[]
for i in range(100):
    aux=str(input('Digite um dos seguintes nomes (Gui, Ana, Bia) \n'))
    if aux == '':
        break
    x.append(aux)
 
Gui=x.count('Gui')
Ana=x.count('Ana')
Bia=x.count('Bia')
 
d={'Ana' : Ana, 'Bia' : Bia, 'Gui' : Gui}
 
for i,j in d.items():
    print('Nome', i, ' : ', j, 'vezes')