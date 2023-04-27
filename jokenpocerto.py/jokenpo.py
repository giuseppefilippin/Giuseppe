from random import randint #biblioteca para aleatoriedade
from time import sleep #biblioteca para pausas
jogo = ['pedra', 'papel', 'tesoura'] #lista de opções jogaveis
confirm = ['continuar', 'sair'] #opção de continuar e sair
while True: # para mostrar os modos de jogo e deixar o usuário escolherx
    opcao = input('''                    -----------JOKENPO-----------
                    1 - Jogador contra computador
                    2 - Jogador contra jogador
                    3 - Computador contra computador
                    Digite seu modo de jogo: ''').strip()
    if opcao in ['1', '2', '3']:
        break
    else:
        print('\33[31mEscolha inválida! Tente novamente.\33[m')
p1 = p2 = 0
if opcao == '1':
    while True: # para o usuário escolher sua jogada
        while True:
            jogador1 = input('\033[34mEscolha entre pedra, papel, tesoura: \033[m').lower().strip()
            if jogador1 in jogo:
                break
            else:
                print('\33[31mEscolha inválida! Tente novamente.\33[m')
        computador = jogo[randint(0, 2)] #escolha do computador
        print(f'\033[36mO computador escolheu: {computador}\033[m')
        if jogador1 == computador:
            print('Empate!!!')
        elif jogador1 == 'pedra' and computador == 'tesoura': #codígo para decidir o ganhador de acordo com as escolhas
            p1 += 1
            print('\033[34mVocê ganhou!!!\033[m')
        elif jogador1 == 'papel' and computador == 'pedra':
            p1 += 1
            print('\033[34mVocê ganhou!!!\033[m')
        elif jogador1 == 'tesoura' and computador == 'papel':
            p1 += 1
            print('\033[34mVocê ganhou!!!\033[m')
        else:
            p2 += 1
            print('\033[36mComputador ganhou!!!\033[m')
        print(f'O placar está {p1} x {p2}')
        while True: # input para continuar o programa ou sair 
            escolha = input('Deseja CONTINUAR ou SAIR? ').lower().strip()
            if escolha in confirm:
                break
            else:
                print('\33[31mEscolha inválida! Tente novamente.\33[m')
        if escolha == 'sair':
            print(f'\033[32mO placar final foi {p1} x {p2}\033[m')
            break
elif opcao == '2':
    while True:
        while True:
            jogador1 = input('\033[34mJogador1: Escolha pedra, papel ou tesoura: \033[m').lower().strip()
            if jogador1 in jogo:
                break
            else:
                print('\33[31mEscolha inválida! Tente novamente.\33[m')
        while True:
            jogador2 = input('\033[36mJogador2: Escolha pedra, papel ou tesoura: \033[m').lower().strip()
            if jogador2 in jogo:
                break
            else:
                print('\33[31mEscolha inválida! Tente novamente.\33[m')
        print(f'\033[34mO jogador1 escolheu: {jogador1}\033[m')
        print(f'\033[36mO jogador2 escolheu: {jogador2}\033[m')
        if jogador1 == jogador2:
            print('Empate!!!')
        elif jogador1 == 'pedra' and jogador2 == 'tesoura':
            p1 += 1
            print('\033[34mJogador1 ganhou!!!\033[m')
        elif jogador1 == 'papel' and jogador2 == 'pedra':
            p1 += 1
            print('\033[34mJogador1 ganhou!!!\033[m')
        elif jogador1 == 'tesoura' and jogador2 == 'papel':
            p1 += 1
            print('\033[34mJogador1 ganhou!!!\033[m')
        else:
            p2 += 1
            print('\033[36mJogador2 ganhou!!!\033[m')
        print(f'O placar está {p1} x {p2}')
        while True:
            escolha = input('Deseja CONTINUAR ou SAIR? ').lower().strip()
            if escolha in confirm:
                break
            else:
                print('\33[31mEscolha inválida! Tente novamente.\33[m')
        if escolha == 'sair':
            print(f'\033[32mO placar final foi {p1} x {p2}\033[m')
            break
elif opcao == '3':
    while True:
        computador1 = jogo[randint(0, 2)]
        computador2 = jogo[randint(0, 2)]
        print(f'\033[34mO computador1 escolheu: {computador1}\033[m')
        print(f'\033[36mO computador2 escolheu: {computador2}\033[m')
        if computador1 == computador2:
            print('Empate!!!')
        elif computador1 == 'pedra' and computador2 == 'tesoura':
            p1 += 1
            print('\033[34mComputador1 ganhou!!!\033[m')
        elif computador1 == 'papel' and computador2 == 'pedra':
            p1 += 1
            print('\033[34mComputador1 ganhou!!!\033[m')
        elif computador1 == 'tesoura' and computador2 == 'papel':
            p1 += 1
            print('\033[34mComputador1 ganhou!!!\033[m')
        else:
            p2 += 1
            print('\033[36mComputador2 ganhou!!!\033[m')
        print(f'O placar está {p1} x {p2}')
        while True:
            escolha = input('Deseja CONTINUAR ou SAIR? ').lower().strip()
            if escolha in confirm:
                break
            else:
                print('\33[31mEscolha inválida! Tente novamente.\33[m')
        if escolha == 'sair':
            print(f'\033[32mO placar final foi {p1} x {p2}\033[m')
            break
nome = ['\033[35mCriadores do código: ', '- Giuseppe Filippin', '- Felipe Baleche', '- Evandro Diniz', 
        '- André Eller', '-Johan Stromberg\033[31m(Rei delas)\33[m' , '- \033[35mTe amamos professora💜\033[m']
for i in range(0, 7):
    print(nome[i])
    sleep(1)