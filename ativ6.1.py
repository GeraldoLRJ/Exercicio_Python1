op=int(input('Digite até qual valor de Fibonacci você deseja imprimir: \n'))
 
x=1
y=0
aux=0
print('\n')
 
for i in range (op):
    print(x)
    aux=x
    x=y+x
    y=aux