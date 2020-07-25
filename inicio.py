import time
from login import Login


class Inicio:

    @staticmethod
    def inic():
        time.sleep(0.5)
        print('Verificando Registros')

        l = True
        while l:
            op = input('1- Verificar login, 2- Sair:')
            if op == '1':
                Login.verificador()
            elif op == '2':
                l = False
                print('Saindo...')
                time.sleep(0.5)
