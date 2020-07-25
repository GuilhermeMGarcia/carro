from gerente import Gerente
from funcgerente import Funcgerente
import time


class Login:

    @staticmethod
    def verificador():
        if Gerente.lst_login == []:
            op = input('Ainda não existe registro cadastrar s/n:')
            if op == 's':
                Gerente(input('Digite nome de usuario:'), input('Digite a senha:'))
            else:
                print('Valtando ao inicio...')
                time.sleep(0.5)
        else:
            print('Ja existe um registro:')
            login = input('Digite o login:')
            senha = input('Digite a senha:')
            if login == Gerente.lst_login[0] and senha == Gerente.lst_senha[0]:
                Funcgerente.terminal()
            else:
                print('Login ou Senha incorreta!')
