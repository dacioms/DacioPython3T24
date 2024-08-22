import random

tentativas = 0
TENTATIVA_MAX = 10

# numero_sorteado = random.randint(1, 100)

numero_sorteado = 35


acertos = False

while tentativas < TENTATIVA_MAX and not acertos:
    try:
        numero_usuario = int(input('Por favor, digite o número sorteado\nNumero escolhido: '))
        if numero_usuario == 999:
            raise Exception('Deu ruim')
    except ValueError as e:
        print('Entrada invalida, digite um número. gerou o erro', e)
        continue
    except Exception as e:
        print('Ocorreu um erro inesperado. Gerou o erro', e)
        continue
    tentativas += 1
    
    if numero_usuario == numero_sorteado:
        acertos = True
        print(f'Parabéns, você acertou o número: {numero_sorteado}')
    elif numero_usuario > numero_sorteado:
        print('Número maior que o sorteado')
    else:
        print('Número menor que o sorteado')    
if not acertos:

    print(f'Número de tentativas esgotados o número sorteado é {numero_sorteado}')