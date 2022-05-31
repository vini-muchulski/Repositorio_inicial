class ContaCorrente:

        def __init__(self, numero, nome, saldo, limite):
            print("Processo 1... {}".format(self))
            self.numero = numero
            self.nome = nome
            self.saldo = saldo
            self.limite = limite

        def extrato(self):
            print("O saldo de {} é R${}.".format(self.nome, self.saldo))

        def deposita(self, valor,):
            self.saldo = self.saldo + valor

        def saca(self, valor,):
            self.saldo = self.saldo - valor

