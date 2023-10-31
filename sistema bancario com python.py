Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ContaBancaria:
...     def __init__(self):
...         self.saldo = 5000.00
...         self.depositos = []
...         self.saques_diarios = 3
...         self.limite_diario = 500.00
... 
...     def depositar(self, valor):
...         if valor > 0:
...             self.saldo += valor
...             self.depositos.append(valor)
...             print(f'Depósito de R${valor:.2f} realizado com sucesso.')
...         else:
...             print('Valor inválido para depósito.')
... 
...     def sacar(self, valor):
...         if self.saques_diarios > 0 and valor <= self.limite_diario and valor <= self.saldo:
...             self.saldo -= valor
...             self.saques_diarios -= 1
...             print(f'Saque de R${valor:.2f} realizado com sucesso.')
...         else:
...             print('Não é possível realizar o saque. Verifique seu saldo ou limite diário de saques.')
... 
...     def extrato(self):
...         print('Extrato da conta:')
...         for i, valor in enumerate(self.depositos, start=1):
...             print(f'Depósito {i}: R${valor:.2f}')
...         print(f'Saldo atual: R${self.saldo:.2f}')
... 
... 
... conta = ContaBancaria()
... 
... # Exemplo de uso:
... conta.depositar(1000)
... conta.sacar(200)
... conta.sacar(600)
... conta.depositar(300)
... conta.sacar(400)
... conta.extrato()
