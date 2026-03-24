<<<<<<< HEAD
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
=======
                                              # Prova pratica de Logica de Programação - CEUB #                                  
# Aluno: Rodrigo de Seabra Vieira   
                                                                # Questão 1 #

#Implemente o programa que gere a sequência dos números naturais na ordem crescente até um valor final fornecido (digitado) pelo usuário. 
#Mostre também a quantidade de valores da sequência gerada. 

valor_final = int(input("Digite o valor final: "))

if valor_final < 0:
    print("Erro: O valor deve ser um número natural (0 ou maior).")

else:
    print("Sequência gerada:")

    for numero in range(valor_final + 1):
        print(numero, end=" ")  

    quantidade = valor_final + 1

    print("")
print(f"Quantidade de valores na sequência: {quantidade}")

                                                                # Questão 2 #
#Implemente o programa que gere a sequência dos números naturais na ordem decrescente até o valor zero e o valor inicial será fornecido (digitado) pelo usuário. 
#Mostre também a quantidade de valores da sequência gerada. 

valor_inicial = int(input("Digite o valor inicial (N): "))

if valor_inicial < 0:
    print("Erro: O valor deve ser um número natural (0 ou maior).")
else:
    print("Sequência gerada:")
        
    for numero in range(valor_inicial, -1, -1):
        print(numero, end=" ")     
    print("") 
        
    quantidade = valor_inicial + 1
    print(f"Quantidade de valores na sequência: {quantidade}")

                                                                # Questão 3 #
#Elabore o programa para somar todos os números inteiros que se encontram no intervalo de um a quinhentos.

numero_inicial = 1
numero_final = 500

soma = 0

for numero in range(numero_inicial, numero):
    soma += numero

print(f"A soma de {numero_inicial} a {numero_final} é: {soma}")

                                                                # Questão 4 #
#Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.

soma_total = 0

for numero in range(1, 501):

    impar = (numero % 2 != 0)
    multiplo = (numero % 3 == 0)
    
    if impar and multiplo:
        soma_total += numero 

print(f"A soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é: {soma_total}")
>>>>>>> 97c2a65d7a761b15a10f496a39d5689c10e23d91
