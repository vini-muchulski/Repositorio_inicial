
class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome= nome
        self.ano= ano
        self.duracao= duracao

topgun2 = Filme("Top Gun: Maverick", 2022, 137)

print("Nome: {} - Ano: {} - Duração: {} Min".format(topgun2.nome,topgun2.ano, topgun2.duracao))


class Serie:
    def __init__(self,nome,ano,temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

twd = Serie("The Walking Dead", 2010,11 )

print("Nome: {} - Ano: {} - Temporadas: {}".format(twd.nome,twd.ano, twd.temporadas))
