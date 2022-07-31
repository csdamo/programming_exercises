class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlsit():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programa = programas

    def __getitem__(self, item):
        return self._programa[item]

    @property
    def listagem(self):
        return self._programa

    def __len__(self):
        return len(self._programa)


vingadores = Filme('poderoso chefão', 1990, 160)
mr_robot = Serie('mr. robot', 2015, 3)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)


mr_robot.dar_like()
mr_robot.dar_like()
mr_robot.dar_like()
vingadores.dar_like()
mr_robot.dar_like()
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, mr_robot, demolidor, tmep]
playlist_fim_de_semana = Playlsit('fim de semana', filmes_e_series)


print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)