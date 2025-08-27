from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Sua escolha: '))
print('=' * 10)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('=' * 10)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Temos um empate')
    elif jogador == 1:
        print('O jogador venceu!')

    elif jogador == 2:
        print('O jogador perdeu!')
    elif jogador >= 3:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
        if jogador == 0:
            print(' O computador venceu!')
        elif jogador == 1:
            print('Empate técnico')
        elif jogador == 2:
                print('O jogador venceu!')
        elif jogador >= 3:
            print('JOGADA INVÁLIDA!')

elif computador == 2:
                if jogador == 0:
                    print('O jogador Ganhou!')
                elif jogador == 1:
                    print('O computador Ganhou!')

                elif jogador == 2:
                    print('JOGO EMPATADO')
                elif jogador >=3:
                    print('JOGADA INVÁLIDA!')



