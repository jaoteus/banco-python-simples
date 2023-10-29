'''
initial commit
'''

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
        self.loop_login = True
        self.loop_principal =True

    #     ''' Funções '''
    #     self.menu()
    
    # def menu(self):
    #     print('D')



Aplication()