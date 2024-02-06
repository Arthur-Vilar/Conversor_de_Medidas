
print('Seja bem vindo ao conversor de medidas. Nosso objetivo é facilitar seu dia a dia.')
print('Opções para conversão:')
print('''[1] = Comprimento(m)
[2] = Capacidade(l)
[3] = Massa(g)''')
while True:
    opc= int(input('Digite sua opção: '))  
    if opc== 1 or opc==2 or opc==3:
        break
#Verificar váriavel e continuar o código.
if opc == 1:
    print('Ótimo, medidas de comprimento então!')
    medida= int(input('''[1]= Quilômetro(Km)
    [2]= Hectômetro(Hm)
    [3]= Decâmetro(Dam)
    [4]= Metro(m)
    [5]= Decímetro(Dm)
    [6]= Centímrtro(Cm)
    [7]= Milímetro(Mm)
    Qual unidade você quer converter? '''))
elif opc == 2:
    print('Beleza, medidas de capacidade!')
elif opc==3:
    print('Medidas de massa, entendi!')
