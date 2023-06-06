import re
import random

nove_digitos = ''
contador_nove_digitos = 10

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

resultado = 0
for digito1 in nove_digitos:
    resultado += int(digito1) * contador_nove_digitos
    contador_nove_digitos -= 1

novo_digito1 = (resultado * 10) % 11
novo_digito1 = novo_digito1 if novo_digito1 <= 9 else 0

dez_digitos = nove_digitos + str(novo_digito1)
contador_dez_digitos = 11

resultado2 = 0
for digito2 in dez_digitos:
    resultado2 += int(digito2) * contador_dez_digitos
    contador_dez_digitos -= 1

novo_digito2 = (resultado2 * 10) % 11
novo_digito2 = novo_digito2 if novo_digito2 <= 9 else 0

cpf_completo = dez_digitos + str(novo_digito2)

print(f'CPF GERADO: {cpf_completo}')

