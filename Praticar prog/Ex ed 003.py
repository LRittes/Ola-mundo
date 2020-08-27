'''•  Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. 
        •	Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo: 
        •	326 = 3 centenas, 2 dezenas e 6 unidades 
        •	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 
'''

while True:
    n1 = int(input('Insira um valor menor que 1000: '))
    c = d = u = 0
    n2 = n1
    if n1 <= 1000:
        while n1>=100:
            n1 -= 100
            c +=1
        while n1 >= 10:
            n1-=10
            d +=1
        while n1 >= 1:
            n1 -=1
            u += 1
        print(f'O valor {n2} tem {c} centenas, {d} dezenas e {u} unidades.')
        break
    else:
        print('ERRO: Valor invalido.')