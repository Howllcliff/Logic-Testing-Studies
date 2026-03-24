class Loja:
    def __init__(self, logradouro, nome, gerente, caixa, meta):
        self.logradouro = logradouro
        self.nome = nome
        self.gerente = gerente
        self.caixa = caixa
        self.meta = meta    

    def get_logradouro(self): return self.lodrasouro
    def get_nome(self): return self.nome
    def get_gerente(self): return self.gerente
    def get_caixa(self): return self.caixa
    def get_meta(self): return self.meta

    def set_logradouro(self, valor): self.logradouro = valor
    def set_nome(self, valor): self.nome = valor
    def set_gerente(self, valor): self.gerente = valor
    def set_caixa(self, valor): self.caixa = valor
    def set_meta(self, valor): self.meta = valor

    def mostra_dados_1(self):
        print(f"Loja: {self.nome} | Endereço: {self.logradouro}")
        print(f"Gerente: {self.gerente} | Caixa: R${self.caixa} | Meta: R${self.meta}")

    def mostra_dados_2(self):
        print(f"Loja: {self.get_nome()} | Endereço: {self.get_logradouro()}")
        print(f"Gerente: {self.get_gerente()} | Caixa: R${self.get_caixa()} | Meta: R${self.get_meta()}")

    def retorna_dados(self):
        return (self.logradouro, self.nome, self.gerente, self.caixa, self.meta)

    def aumentar_meta(self, valor_aumento):
        self.meta += valor_aumento
        print(f"Meta atualizada com sucesso para: R${self.meta}")

    def verificar_desempenho(self):
        if self.meta <= 0:
            porcentagem = 100
        else:
            porcentagem = (self.caixa / self.meta) * 100
        
        status = "META ATINGIDA" if porcentagem >= 100 else "EM ANDAMENTO"
        print(f"Desempenho da Loja {self.nome}: {porcentagem:.2f}% ({status})")

if __name__ == "__main__":

    loja1 = Loja("Asa Sul", "Bar do Dev", "Carlos", 1500, 5000)
    loja2 = Loja("Águas Claras", "Tech Coffee", "Ana", 800, 2000)
    loja3 = Loja("Taguatinga", "Mega Store", "Bruno", 6000, 5500)
    loja4 = Loja("Guará", "Pet Shop", "Julia", 300, 1000)

    print(f"\n--- Atualização de Meta para {loja1.get_nome()} ---")
    try:
        valor = float(input("Digite o valor para aumentar a meta da loja: "))
        loja1.aumentar_meta(valor)
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
    
    loja1.mostra_dados_1()
    loja2.mostra_dados_2()

    loja3.set_gerente("Ricardo")
    print(f"Novo gerente da loja 3: {loja3.get_gerente()}")

    dados_loja4 = loja4.retorna_dados()
    print(f"Tupla de dados da loja 4: {dados_loja4}")

    loja1.verificar_desempenho()
    loja3.verificar_desempenho()