op=int(input('Digite até qual valor fatorial deseja imprimir: \n'))
 
x=op
y=op-1
 
print('\n')
 
while y > 0:
 
    x=y*x
    y=y-1
 
if op == 1 or op == 0:
    x=1
   
print(x)