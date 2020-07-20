class Carro:
    lst = []
    lstmarca = []

    def __init__(self, marca, valor, cor, ano):
        self.marca = marca
        self.valor = valor
        self.cor = cor
        self.ano = ano
        long = f'Marca:{self.marca} Valor:{self.valor} Cor:{self.cor} Ano:{self.ano}'
        Carro.lst.append(long)
        long2 = f'Marca:{marca}'
        Carro.lstmarca.append(long2)
        print(f'{self.marca} adicionado!')

    @staticmethod
    def imprimir():
        if Carro.lst != []:
            count = 0
            for i in Carro.lst:
                print(f'{count + 1}º {i} ')
                count =+ 1
        else:
            print('Lista de Carros Vazias!')

    @staticmethod
    def excluir():
        if Carro.lst != []:
            count = 0
            for i in Carro.lstmarca:
                print(f'{count + 1}º {i} ')
                count =+ 1
            op = int(input(f'Digite o numero que deseja Excluir:'))
            op =- 1
            j = str(Carro.lst[op])
            print(f'{j} removido')
            Carro.lst.remove(j)
            if Carro.lst != []:
                count2 = 0
                print('Carros Sobrando:')
                for a in Carro.lst:
                    print(f'{count2 + 1 }º {a} ')
                    count2 =+ 1
        else:
            print('Lista de Carros Vazias!')



