                                              # Prova pratica de Logica de Programação - CEUB #                                  
# Aluno: Rodrigo de Seabra Vieira   
                                                                # Questão 1 #

print("\n------- Questão 1 PP3 -- Rodrigo Vieira -------")
print("Digite os números inteiros, Para finalizar: Digite '0'.\n")

soma_pares = 0
contagem_pares = 0  
soma_impares = 0
contagem_impares = 0

while True:
    try:
        entrada = input("Digite um número: ")
        numero = float(entrada)

        if numero == 0:
            print("\nNúmero 0 digitado. Finalizando a coleta dos números")
            break
        elif numero % 2 == 0:
            soma_pares += numero
            contagem_pares += 1
        else:
            soma_impares += numero
            contagem_impares += 1
                
    except ValueError:
            print(f" '{entrada}' Não é um número inteiro válido. Tente novamente.")

print("\n--- Resultados Finais ---\n")
    
if contagem_pares > 0:
    media_pares = soma_pares / contagem_pares
    print(f"Média dos números pares: {media_pares:.3f}\n")
else:
    print("Nenhum número par foi digitado.")
        
if contagem_impares > 0:
    media_impares = soma_impares / contagem_impares
    print(f"Média dos números ímpares: {media_impares:.3f}\n")
else:
    print("Nenhum número ímpar foi digitado.\n")


                                                                # Questão 2 #


print("\n------- Questão 2 PP3 -- Rodrigo Vieira -------\n")
print("Digite os números Reais, Para finalizar: Digite '0'.\n")

contagem = 0
soma_numeros = 0
maior_valor = None
menor_valor = None
qtd_50 = 0
while True:
    try:
        entrada = input("Digite um número: ")
        numero = float(entrada)

        if numero == 0:
            print("\nNúmero 0 digitado. Finalizando a coleta dos números")
            break
        else:
            contagem += 1
            soma_numeros += numero    
            if numero >= 50:
                qtd_50 += 1

            if maior_valor is None:
                maior_valor = numero
                menor_valor = numero
            else:
              if numero > maior_valor:
                maior_valor = numero
              if numero < menor_valor:
                menor_valor = numero   
    except ValueError:
            print(f" '{entrada}' Não é um número válido. Tente novamente.")

print("\n--- Pedidos da Questão ---\n")

if contagem > 0:
    media = soma_numeros / contagem
    print(f"1. Quantidade de valores digitados: {contagem}")
    print(f"2. Soma dos valores digitados: {soma_numeros:.3f}")
    print(f"3. Média aritmética dos valores: {media:.3f}")
    print(f"4. Maior valor digitado: {maior_valor:.3f}")
    print(f"5. Menor valor digitado: {menor_valor:.3f}")
    print(f"6. Quantidade de valores maior ou igual a 50: {qtd_50}")
else:
    print("Nenhum valor foi digitado para análise.")


                                                                    #Brasilia - DF 09/09/2025