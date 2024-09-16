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
quantidade_positivo_negativo=[]
maior_numero = 0
menor_numero = 0

quantidade_numero=5

# Variáveis para armazenar os números
for i in range(quantidade_numero):
    numero = int(input(f"digite seu  {i+1}ª numero: "))
    lista_numero.append(numero)
    break

#processando cada numero
def verificar_pares_impares(numero):
    qtd_pares=0
    qtd_impares=0
    for numero in numero:
        if numero % 2 == 0:
            qtd_pares +=1
        else:
            qtd_impares +=1
   

# Calculando as médias

# Mostrando números na ordem inversa
pares,impares=verificar_pares_impares(lista_numero)
for i in range (quantidade_numero):
    numero=int(input(f"digite o {i+1}ª: numero "))

print(f"quantidade de pares: {quantidade_pares} ")
print(f"quantidadede impares: {quantidade_impares} ")


