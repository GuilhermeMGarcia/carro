import time
from carro import Carro

print('Carregando...')
time.sleep(0.5)
print('Bem Vindo a concecionaria de carros')

print('Selecione uma das opções.')

loop = True
while loop:
    op = input('Opção 1- Adicionar Carros, 2- Ver Carros, 3- Excluir, 4- Sair.:').upper()
    if op == '1':
        try:
            Carro(marca=input('Digite a Marca:'), valor=int(input('Digite o valor:')), cor=input('Digite a cor:'), ano=int(input('Digite o ano:')))
        except ValueError:
            print('Opção invalida')
    if op == '2':
        Carro.imprimir()
    if op == '3':
        Carro.excluir()
    if op == '4':
        loop = False