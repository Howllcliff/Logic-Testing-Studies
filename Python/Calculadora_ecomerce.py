def normal_free(frete, valor_produto):
    normal = valor_produto + frete
    return normal
def premium(valor_produto, taxa):
    premium = (valor_produto) / (1 - ( taxa / 100))
    return premium


if __name__ == '__main__':
    print(f"\n\n ------- Calculadora para E-Commerces -------\n")
    valor_produto = float(input("Digite o Valor do Produto: "))
    valor_taxa = float(input("Digite o Valor da Taxa (0 - 100%): "))
    valor_frete = float(input("Digite o Valor do Frete: "))
    free_plan = normal_free(valor_produto, valor_frete)
    premium_plan = premium(valor_produto, valor_taxa)

    print(f"   ------- Os Valores são: -------   \n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Sem Plano ou Frete é: {valor_produto:.2f}R$\n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Sem Plano com Frete é: {free_plan:.2f}R$\n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Com Plano de {valor_taxa:.0f}% sem Frete de {valor_frete:.2f}R$ é: {premium_plan:.2f}R$\n")
    print(f"O Valor do Desejado é: {valor_produto:.2f}R$\n      Venda Com Plano de {valor_taxa:.0f}% com Frete de {valor_frete:.2f}R$ é: {premium_plan + valor_frete:.2f}R$\n")


    