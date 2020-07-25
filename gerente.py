class Gerente:
    lst_login = []
    lst_senha = []
    lst_nome = []

    def __init__(self, login, senha, nome):
        self.login = login
        Gerente.lst_login.append(self.login)
        self.senha = senha
        Gerente.lst_senha.append(self.senha)
        self.nome = nome
        Gerente.lst_nome.append(self.nome)
