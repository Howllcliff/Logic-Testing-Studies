class Player:
    def __init__(self, nome, vida , playerxp, nivel, id_player=None):
        self.nome = nome
        self.vida = vida
        self.playerxp = playerxp
        self.nivel = nivel
        self.id_player = id_player
    def get_nome(self):
        return self.nome
    def get_vida(self):
        return self.vida
    def get_playerxp(self):
        return self.playerxp
    def get_nivel(self):
        return self.nivel
    def get_id_player(self):
        return self.id_player

    def set_nome(self,novonome):
        self.nome = novonome
    def set_vida(self,novavida):
        self.vida = novavida
    def set_playerxp(self,novoplayerxp):
        self.playerxp = novoplayerxp
    def set_nivel(self,novonivel):
        self.nivel = novonivel

    def mostrar_player(self):
        print(f"Nome:{self.nome} --- Vida:{self.vida} --- Experiencia:{self.playerxp} --- Nivel:{self.nivel} --- ID:{self.id_player}")

    def aumento_xp(self,novoxp):
        self.playerxp += novoxp

if __name__ == "__main__":

    print(f"\n{'-'*21}# Prova Pratica 1 1.2026 #{'-'*21}")

    lista_players = []

    for i in range(4):
        nome = str(input("Digite o nome do Jogador(Digite 0 para SAIR): "))
        if nome == "0":
            break
        vida = float(input("Digite a vida base do jogador: "))
        experiencia = int(input("Digite a experiencia base do jogador: "))
        nivel = int(input("Digite o nivel base do jogador: "))

        novoplayer = Player(nome, vida, experiencia, nivel)
        lista_players.append(novoplayer)

    print(f"\n{'-'*15} LISTA DE JOGADORES CADASTRADOS {'-'*15}")
    for player in lista_players:
        player.mostrar_player()

    lista_players[2].set_nome("Lucas")

    print(f"\n{'-'*15} LISTA DE JOGADORES CADASTRADOS {'-'*15}")
    for player in lista_players:
        player.mostrar_player()    

    aumento_de_exp = 100
    id_player = int(input("\nQual player vai receber a exp:"))
    lista_players[id_player].aumento_xp(aumento_de_exp)

    print(f"\n{'-'*15} LISTA DE JOGADORES CADASTRADOS {'-'*15}")
