'''
initial commit
'''
import os

class Aplication():
    def __init__(self) -> None:
        ''' Variáveis '''
        self.saldo_cc = 0.0
        self.saldo_cp = 0.0
        self.valor = 0.0
        self.nome_titular = 'John'
        self.senha = 'john0011'
        self.CPF = '000.000.000-11'
        self.numero_conta_corrente = '1234-1'
        self.numero_conta_poupanca = '1234-2'
        self.agencia = '2332-9'
        self.endereco = 'Rua Seilá, n°01, Recife, Pernambuco.'
        self.numero = '+55 00 0000-1111'
        self.opcao_menu = ''
        self.email = 'john0011@gmail.com'

        ''' Loops '''
        self.loop_menu = True
        self.loop_principal =True

        ''' Flags '''
        self.autenticado = None

        ''' Funções '''
        self.login()
        self.menu()

    def login(self):
        while self.autenticado == None:
            self.email_ou_cpf = str(input('Digite seu e-mail ou CPF: '))
            self.senha_login = str(input('Digite sua senha: '))
            if (self.email_ou_cpf == self.email or self.email_ou_cpf == self.CPF and self.senha_login == self.senha):
                os.system('cls')
                print("Login efetuado com sucesso!")
                self.autenticado = True
            elif (self.email_ou_cpf == '' or self.senha_login == ''):
                os.system('cls')
                print("Alguns dos campos ficaram em branco, tente novamente!")
                continue
            else:
                os.system('cls')
                print("E-mail, CPF ou senha incorretos, tente novamente!")
                continue

    def menu(self):
        print('1 - Dados da conta')
        print('2 - Depósito na conta corrente')
        print('3 - Saque na conta corrente')
        print('4 - Depósito na conta poupança')
        print('5 - Resgate na conta poupança')
        print('6 - Sair')
        while self.loop_menu:
            self.valor = str(input("Digite: "))
            match self.valor:
                case '1':
                    # Dados da conta
                    break
                case '2':
                    # Depósito conta corrente
                    break
                case '3':
                    # 



Aplication()