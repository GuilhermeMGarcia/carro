from gerente import Gerente


class Login:

    @staticmethod
    def verificador(self):
        if Gerente.lst_login == []:
            login, senha = Gerente(input('Digite nome de usuario:'), input('Digite a senha;'))
        else:
            print('È permitido somente um cadastro!')