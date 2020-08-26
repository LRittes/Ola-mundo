n1 = int(input('Insira o dia: '))
n2 = int(input('Mês: '))
n3 = int(input('Ano: '))
            
if 0 <= n1 <= 31 and 1 <= n2 <= 12 and 0 <= n3 <= 2020:
    print(f'A data {n1}/{n2}/{n3} é valida!')
else:
    print('\033[1;31mErro: data invalida!\033[m')