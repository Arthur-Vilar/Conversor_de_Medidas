def l():
    print('-'*35)
from time import sleep
print('-'*80)
print('Seja bem vindo ao conversor de medidas. Nosso objetivo é facilitar seu dia a dia.')
print('-'*80)
print('Opções para conversão:')
print('''[1] = \033[35mComprimento(m)\033[m
[2] = \033[34mCapacidade(l)\033[m
[3] = \033[36mMassa(g)\033[m
[4] = \033[31;41mSair\033[m''')

while True:
    opc= int(input('Digite sua opção: '))  
    l()
    if opc== 1 or opc==2 or opc==3 or opc==4:
        break

if opc == 1:
    print('Ótimo, medidas de \033[34mcomprimento\033[m então!')
    l()
    medida= int(input('''    \033[31m[1]= Quilômetro(Km)\033[m
    \033[32m[2]= Hectômetro(Hm)\033[m 
    \033[33m[3]= Decâmetro(Dam)\033[m
    [4]= Metro(m)
    \033[34m[5]= Decímetro(Dm)\033[m
    \033[35m[6]= Centímetro(Cm)\033[m
    \033[36m[7]= Milímetro(Mm)\033[m
    Qual unidade você quer converter? '''))
    while medida not in range(1,8):
        medida= int(input('         \033[31mOpção inválida!\033[m Digite novamente: '))
    quantidade= int(input('    Digite o quantidade da medida que você quer converter: '))
    if medida == 1:
        print(f'''{quantidade}km -> {quantidade*10}hm -> {quantidade*100}dam -> {quantidade*1000}m -> {quantidade*10000}dm -> {quantidade*100000}cm -> {quantidade*1000000}mm''')
    if medida == 2:
        print(f'''{quantidade/10}km -> {quantidade}hm -> {quantidade*10}dam -> {quantidade*100}m -> {quantidade*1000}dm -> {quantidade*10000}cm -> {quantidade*100000}mm''')
    if medida == 3:
        print(f'''{quantidade/100}km -> {quantidade/10}hm -> {quantidade}dam -> {quantidade*10}m -> {quantidade*100}dm -> {quantidade*1000}cm -> {quantidade*10000}mm''')
    if medida == 4:
        print(f'''{quantidade/1000}km -> {quantidade/100}hm -> {quantidade/10}dam -> {quantidade}m -> {quantidade*10}dm -> {quantidade*100}cm -> {quantidade*1000}mm''')
    if medida == 5:
        print(f'''{quantidade/10000}km -> {quantidade/1000}hm -> {quantidade/100}dam -> {quantidade/10}m ->{quantidade}dm -> {quantidade*10}cm -> {quantidade*100}mm''')
    if medida == 6:
        print(f'''{quantidade/100000}km -> {quantidade/10000}hm -> {quantidade/1000}dam -> {quantidade/100}m ->{quantidade/10}dm -> {quantidade}cm -> {quantidade*10}mm''')
    if medida == 7:
        print(f'''{quantidade/1000000}km -> {quantidade/100000}hm -> {quantidade/10000}dam -> {quantidade/1000}m ->{quantidade/100}dm -> {quantidade/10}cm -> {quantidade}mm''')

elif opc == 2:
    print('Beleza, medidas de \033[34mcapacidade\033[m!')
    l()
    medida= int(input('''    \033[31m[1]= Quilolitro(Kl)\033[m
    \033[32m[2]= Hectolitro(Hl)\033[m
    \033[33m[3]= Decalitro(Dal)\033[m
    [4]= Litro(l)
    \033[34m[5]= Decilitro(Dl)\033[m
    \033[35m[6]= Centilitro(Cl)\033[m
    \033[36m[7]= Mililitro(Ml)\033[m
    Qual unidade você quer converter? '''))
    while medida not in range(1,8):
        medida= int(input('         \033[31mOpção inválida!\033[m Digite novamente: '))
    quantidade= int(input('    Digite a quantidade da medida que você quer converter: '))
    if medida == 1:
        print(f'''{quantidade}kl -> {quantidade*10}hl -> {quantidade*100}dal -> {quantidade*1000}l -> {quantidade*10000}dl -> {quantidade*100000}cl -> {quantidade*1000000}ml''')
    if medida == 2:
        print(f'''{quantidade/10}kl -> {quantidade}hl -> {quantidade*10}dal -> {quantidade*100}l -> {quantidade*1000}dl -> {quantidade*10000}cl -> {quantidade*100000}ml''')
    if medida == 3:
        print(f'''{quantidade/100}kl -> {quantidade/10}hl -> {quantidade}dal -> {quantidade*10}l -> {quantidade*100}dl -> {quantidade*1000}cl -> {quantidade*10000}ml''')
    if medida == 4:
        print(f'''{quantidade/1000}kl -> {quantidade/100}hl -> {quantidade/10}dal -> {quantidade}l -> {quantidade*10}dl -> {quantidade*100}cl -> {quantidade*1000}ml''')
    if medida == 5:
        print(f'''{quantidade/10000}kl -> {quantidade/1000}hl -> {quantidade/100}dal -> {quantidade/10}l ->{quantidade}dl -> {quantidade*10}cl -> {quantidade*100}ml''')
    if medida == 6:
        print(f'''{quantidade/100000}kl -> {quantidade/10000}hl -> {quantidade/1000}dal -> {quantidade/100}l ->{quantidade/10}dl -> {quantidade}cl -> {quantidade*10}ml''')
    if medida == 7:
        print(f'''{quantidade/1000000}kl -> {quantidade/100000}hl -> {quantidade/10000}dal -> {quantidade/1000}l ->{quantidade/100}dl -> {quantidade/10}cl -> {quantidade}ml''')

elif opc==3:
    print('Medidas de \033[34mmassa\033[m, entendido!')
    l()
    medida= int(input('''    \033[31m[1]= Quilograma(Kg)\033[m
    \033[32m[2]= Hectograma(Hg)\033[m
    \033[33m[3]= Decagrama(Dag)\033[m
    [4]= Grama(g)
    \033[34m[5]= Decigrama(Dg)\033[m
    \033[35m[6]= Centigrama(Cg)\033[m
    \033[36m[7]= Miligrama(Mg)\033[m
    Qual unidade você quer converter? '''))
    while medida not in range(1,8):
        medida= int(input('         \033[31mOpção inválida!\033[m Digite novamente: '))
    quantidade= int(input('    Digite a quantidade da medida que você quer converter: '))

    if medida == 1:
        print(f'''{quantidade}kg -> {quantidade*10}hg -> {quantidade*100}dag -> {quantidade*1000}g -> {quantidade*10000}dg -> {quantidade*100000}cg -> {quantidade*1000000}mg''')
    if medida == 2:
        print(f'''{quantidade/10}kg -> {quantidade}hg -> {quantidade*10}dag -> {quantidade*100}g -> {quantidade*1000}dg -> {quantidade*10000}cg -> {quantidade*100000}mg''')
    if medida == 3:
        print(f'''{quantidade/100}kg -> {quantidade/10}hg -> {quantidade}dag -> {quantidade*10}g -> {quantidade*100}dg -> {quantidade*1000}cg -> {quantidade*10000}mg''')
    if medida == 4:
        print(f'''{quantidade/1000}kg -> {quantidade/100}hg -> {quantidade/10}dag -> {quantidade}g -> {quantidade*10}dg -> {quantidade*100}cg -> {quantidade*1000}mg''')
    if medida == 5:
        print(f'''{quantidade/10000}kg -> {quantidade/1000}hg -> {quantidade/100}dag -> {quantidade/10}g ->{quantidade}dg -> {quantidade*10}cg -> {quantidade*100}mg''')
    if medida == 6:
        print(f'''{quantidade/100000}kg -> {quantidade/10000}hg -> {quantidade/1000}dag -> {quantidade/100}g ->{quantidade/10}dg -> {quantidade}cg -> {quantidade*10}mg''')
    if medida == 7:
        print(f'''{quantidade/1000000}kg -> {quantidade/100000}hg -> {quantidade/10000}dag -> {quantidade/1000}g ->{quantidade/100}dg -> {quantidade/10}cg -> {quantidade}mg''')
elif opc==4:
    pass
l()
print('Encerrando programa...')
sleep(1)
print('\033[32mPrograma encerrado com sucesso, volte sempre!\033[m')