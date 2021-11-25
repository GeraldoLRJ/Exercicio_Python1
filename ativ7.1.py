x=['Ana', 'Bia', 'Gui', 'Gui', 'Ana', 'Ana']
Gui=x.count('Gui')
Ana=x.count('Ana')
Bia=x.count('Bia')
 
d={'Ana' : Ana, 'Bia' : Bia, 'Gui' : Gui}
for i,j in d.items():
    print('Nome', i, ' : ', j, 'vezes')