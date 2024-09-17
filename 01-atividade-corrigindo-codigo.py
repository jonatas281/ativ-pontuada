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
qtd_numero=5
lista_numero=[]
contador_pares=0
contador_impares=0
contador_positivo=0
contador_negativo=0
pares=0
impares=0
numero=0
for i in range (qtd_numero):
    while True:
     numero = int(input(f"digite o {i+1}º: "))
     numero.append(numero)

#verificar pares e impares:

     if numero % 2 == 0:
       contador_pares +=1
     else:
       contador_impares +=1

if len(pares) > 0:
    media_pares = sum(pares) / len(pares)
else:
    media_pares = 0

if len(impares) > 0:
    media_impares = sum(impares) / len(impares)
else:
    media_impares= 0

#verificar positivo negativo
if numero >=0:
  contador_positivo +=1
else:
  contador_negativo +=1

for numero in reversed(lista_numero):
    print(numero) 


print(f"quantidade de numeros pares: {contador_pares}")
print(f"quantidade de numeros impares: {contador_impares}")
print(f"quantidade de numero positivo: {contador_positivo}")
print(f"quantidade de numero negarivo: {contador_negativo}")
print(f"media de pares: {media_pares}")
print(f"media de inpares: {media_impares}")
 
