import random
import re
import time

# Gerador de placas mercosul
chars_a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars_n = '0123456789'

# Cor para o terminal
cor_verde = '\033[92m'
reset_cor = '\033[0m'

# Expressão regular para placas Mercosul (ABC1D23)
regex_placa = re.compile(r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$')

# Quantidade de placas que serão geradas
while True:
    try:
        quantidade = int(input('Quantas placas você gostaria de gerar?  '))
        if quantidade <= 0:
            print("A quantidade deve ser um número positivo.")
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print(f'Quantidade inválida, tente novamente.')

# Loop for para imprimir as placas para o usuário
numero = 0

# Efeito para gerar as placas
print('Gerando...\n')
time.sleep(1)

for placas in range(quantidade):

    time.sleep(0.10)

    a1 = random.choice(chars_n)
    a2 = random.choice(chars_a)
    a3 = random.choice(chars_a)
    n1 = random.choice(chars_n)
    a4 = random.choice(chars_a)
    n2 = random.choice(chars_n)
    n3 = random.choice(chars_n)

    numero += 1

    placa = a1 + a2 + a3 + n1 + a4 + n2 + n3

    # Verificar se a placa está no formato correto
    if regex_placa.match(placa):
        validacao = "Válida ✅"
    else:
        validacao = "Inválida ❌"
    print(f'PLACA {numero}: {cor_verde}{placa}{reset_cor} - {validacao}')
