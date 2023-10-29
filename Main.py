'''
initial commit
'''
import os

class Aplication:
    def __init__(self):
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
        self.flag = None

        ''' Funções '''
        # self.login()     
        self.menu()

    # def login(self):
    #     while self.autenticado == None:
    #         self.email_ou_cpf = str(input('Digite seu e-mail ou CPF: '))
    #         self.senha_login = str(input('Digite sua senha: '))
    #         if (self.email_ou_cpf == self.email or self.email_ou_cpf == self.CPF and self.senha_login == self.senha):
    #             os.system('cls')
    #             print("Login efetuado com sucesso!")
    #             self.autenticado = True
    #         elif (self.email_ou_cpf == '' or self.senha_login == ''):
    #             os.system('cls')
    #             print("Alguns dos campos ficaram em branco, tente novamente!")
    #             continue
    #         else:
    #             os.system('cls')
    #             print("E-mail, CPF ou senha incorretos, tente novamente!")
    #             continue

    def menu(self):
        ''' Menu Principal'''
        print('1 - Dados da conta')
        print('2 - Depósito na conta corrente')
        print('3 - Saque na conta corrente')
        print('4 - Depósito na conta poupança')
        print('5 - Resgate na conta poupança')
        print('6 - Sair')

        while self.loop_menu:
            self.opcao_menu = str(input("Digite: "))
            match self.opcao_menu:
                case '1':
                    # Dados da conta
                    self.mostrar_dados()
                    break
                case '2':
                    # Depósito conta corrente
                    self.deposito_cc()
                    break
                case '3':
                    # Saque na conra corrente
                    self.saque_cc()
                    break
                case '4':
                    # Deposito na conta poupanca
                    print("Funcionou")
                    break
                case '5':
                    # resgate na conta poupanca
                    print("Funcionou")
                    break
                case '6':
                    # Sair
                    print("Funcionou")
                    break
                case '':
                    print("Você não digitou nada!")
                    print("Funcionou")
                    break

    def mostrar_dados(self):
        ''' Mostrar dados do usuário '''
        os.system('cls')
        print(f'Seu nome: {self.nome_titular}')
        print(f'Sua agência: {self.agencia}')
        print(f'Conta corrente: {self.numero_conta_corrente}')
        print(f'Conta poupança: {self.numero_conta_poupanca}')
        print(f'Número de telefone: {self.numero}')
        print(f'E-mail: {self.email}')
        print(f'CPF: {self.CPF}')
        print(f'Endereço: {self.endereco}')
        print(f'Senha: ********')
        print(f'Saldo conta corrente: {self.saldo_cc}')
        print(f'Saldo conta poupança: {self.saldo_cp}')
        self.menu()

        return None
    
    def deposito_cc(self):
        self.flag = None
        while self.flag == None:
            try:
                self.valor = float(input("Para cancelar, clique ENTER\nDigite o valor para depósito: "))
            except ValueError:
                print("O valor deve ser númerico!")
                continue
            else:
                while self.flag == None:
                    print(f'Você está prestes a depositar R${self.valor} na sua conta corrente, deseja continuar ?\nS - Sim\nN - Não')
                    self.opcao_menu = str(input('Digite: '))
                    if self.opcao_menu == 'S' or self.opcao_menu == 's':
                        self.saldo_cc = self.saldo_cc + self.valor
                        self.flag = True
                        os.system('cls')
                        print(
                            f'Depósito no valor de R${self.valor} depositado com sucesso!\n'
                            f'Agora o seu saldo da conta corrente é de R${self.saldo_cc} :)'
                            )
                        self.menu()
                    elif self.opcao_menu != 'S' or self.opcao_menu != 's':
                        os.system('cls')
                        self.flag = True
                        print(
                            "Operação cancelada com sucesso!\n"
                            f'O saldo da sua conta corrente permanece em R${self.saldo_cc} :)'
                            )
                        self.menu()

    def saque_cc(self):
        self.flag = None
        self.result = 0.0
        while self.flag == None:
            try:
                self.valor = float(input("Digite o valor desejado para o saque: "))
                
                if self.valor > self.saldo_cc:
                    print(
                        "Saldo insuficiente :(\n"
                        f'Seu saldo é de R${self.saldo_cc}'
                        )
                    self.opcao_menu = input(
                        'Deseja depositar na sua conta corrente ?\n'
                        'S - Sim\n'
                        'N - Não\n'
                        'Digite: '
                        )
                    if self.opcao_menu == 'S' or self.opcao_menu == 's':
                        self.flag = True
                        os.system('cls')
                        self.deposito_cc()
                    else:
                        self.flag = True
                        os.system('cls')
                        self.menu()
                else:
                    pass
            except ValueError:
                print("O valor deve ser númerico!")
                continue
            else:
                while self.flag == None:
                    print(
                        f'Você está prestes a sacar R${self.valor} da sua conta corrente, deseja continuar ?\n'
                        'S - Sim\n'
                        'N - Não\n'
                        )
                    self.opcao_menu = str(input('Digite: '))
                    if self.opcao_menu == 'S' or self.opcao_menu =='s':
                        self.saldo_cc = self.saldo_cc - self.valor
                        os.system('cls')
                        self.menu()
                        print(
                            f'Saque no valor de R${self.valor} efetuado com sucesso!'
                            f'O seu saldo da conta corrente agora é de R${self.saldo_cc}'
                        )

                
    def atualizar_dados(self):
        ''' Atualizar dados do usuário'''
        pass

Aplication()