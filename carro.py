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


    def imprimir(self):
        if Carro.lst != []:
            count = 0
            for i in Carro.lst:
                print(f'{count + 1}º {i} ')
                count =+ 1
        else:
            print('Lista de Carros Vazias!')


    def excluir(self):
        if Carro.lst != []:
            count = 0
            for i in Carro.lstmarca:
                print(f'{count + 1}º {i} ')
                count =+ 1
            op = int(input(f'Digite o numero que deseja Excluir:'))
            op2 = op
            op -= 1
            a = len(Carro.lst)
            if op2 <= 0 or op2 > a:
                print('Opção invalida')
            else:
                j = str(Carro.lst[op])
                print(f'{j} removido')
                Carro.lst.remove(j)
                j1 = str(Carro.lstmarca[op])
                Carro.lstmarca.remove(j1)
                if Carro.lst != []:
                    count2 = 0
                    print('Carros Sobrando:')
                    for a in Carro.lst:
                        print(f'{count2 + 1 }º {a} ')
                        count2 += 1
        else:
            print('Lista de Carros Vazias!')



