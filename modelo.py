class Programa:
        def __init__(self, nome, ano):
            self._nome = nome.title()
            self.ano = ano
            self._likes = 0

        @property
        def likes(self):
            return self._likes

        def curtida(self):
            self._likes += 1

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, novo_nome):
            self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        
        self.duracao = duracao



class Serie(Programa):
    def __init__(self,nome ,ano ,temporadas):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.temporadas = temporadas



twd = Serie("the walking dead", 2010,11,)

twd.curtida()
twd.curtida()
twd.curtida()
twd.curtida()

print("Nome: {} - Ano: {} - Temporadas: {} - Curtidas {}".format(twd.nome,twd.ano, twd.temporadas,twd.likes))

topgun2 = Filme("top gun: maverick", 2022, 137, )
topgun2.curtida()
topgun2.curtida()
topgun2.curtida()


print("Nome: {} - Ano: {} - Duração: {} Min - Curtidas {}".format(topgun2.nome,topgun2.ano, topgun2.duracao,topgun2.likes))