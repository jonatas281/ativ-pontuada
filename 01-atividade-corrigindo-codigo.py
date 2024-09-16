import os 
os . system ("cls || clear" )
"""
1. A quantidade de números pares e ímpares.
2. A quantidade de números positivos e negativos.
3. A quantidade de números inseridos.
4. O maior e o menor número.
5. A média de números pares.
6. A média de números ímpares.
7. A média de todos os números inseridos.
8. Mostrar os números lidos na ordem inversa.
"""
# Variáveis para armazenar as estatísticas
lista_numero=[]
quantidade_pares=0
quantidade_impares=0
quantidade_positivo_negativo=0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
quantidade_numero=5

# Variáveis para armazenar os números
for i in range(quantidade_numero):
    numero = int(input(f"digite seu  {i+1}ª numero: "))
    lista_numero.append(numero)
    break

#processando cada numero
def verificar_pares_impares(numero):
    if numero %2 == 0:
        quantidade_pares +=1
    else:
        quantidade_impares +=1
    return quantidade_pares,quantidade_impares






# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

# Mostrando números na ordem inversa


# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa: {numeros_invertidos}")