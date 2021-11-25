print('Escolha qual calculo deseja realizar: \n 1-Adição \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n 5-Sair \n')
op=int(input())
 
x=float(input('Digite um valor '))
y=float(input('Digite outro valor '))
 
if op == 1:
    x+=y
elif op == 2:
    x-=y
elif op == 3:
    x=x*y
elif op == 4:
    x=x/y
else:
    print('Opção Inválida')
 
print('Resultado: ',x)