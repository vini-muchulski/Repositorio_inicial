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

        def get_saldo(self):
            return self.__saldo

        def get_nome(self):
            return self.__nome

        def get_limite(self):
            return self.__limite

        def set_limit(self,limite):
            self.__limite = limite


