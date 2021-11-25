op=int(input('Digite até qual valor fatorial deseja imprimir: \n'))
 
x=op
y=op-1
 
print('\n')
 
for i in range (op-1):
   
    x=y*x
    y=y-1
if x == 0:
    x=1
print(x)