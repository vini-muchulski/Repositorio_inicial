class ContaCorrente:

        def __init__(self, numero, nome, saldo, limite):
            print("Processo 1... {}".format(self))
            self.__numero = numero
            self.__nome = nome
            self.__saldo = saldo
            self.__limite = limite

        def extrato(self):
            print("O saldo de {} é R${}.".format(self.__nome, self.__saldo))

        def depositar(self, valor,):
            self.__saldo = self.__saldo + valor

        def sacar(self, valor,):
            self.__saldo = self.__saldo - valor

        def transferir(self,valor, destino):
            self.sacar(valor)
            destino.depositar(valor)


