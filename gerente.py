class Gerente:
    lst_login = []
    lst_senha = []

    def __init__(self, login, senha):
        self.login = login
        Gerente.lst_login.append(self.login)
        self.senha = senha
        Gerente.lst_senha.append(self.senha)
