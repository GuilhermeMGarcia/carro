class Carro:
    lst = []
    lstmarca = []

    def __init__(self, marca, valor):
        self.marca = marca
        self.valor = valor
        long = f'Marca:{self.marca} Valor:{self.valor}'
        Carro.lst.append(long)
        long2 = f'Marca:{marca}'
        Carro.lstmarca.append(long2)
        print(f'{self.marca} adicionado!')

    @staticmethod
    def imprimir():
        long = Carro.lst
        if long != []:
            print('-----------')
            print(*long)
            print(f'lista normal:{Carro.lst}')
            print(len(Carro.lst))
            print('-----------')
        else:
            print('N existe nenhum carro adicionado.')

    @staticmethod
    def excluir():
        long = Carro.lst
        if long != []:
            print('Qual modelo deseja excluir:')
            print(*long)
            op = f'Marca:{input()}'
            for i in range (len(Carro.lst)):
                for j in Carro.lst:
                    if j == op:
                         print(f'{op} removido!') #erro ao excluir
                         Carro.lst[i].remove(op)
                         print('deu certo')
            else:
                print('Modelo n existe!')

        else:
            print('N existe nenhum carro adicionado.')
