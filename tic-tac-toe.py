def mostrar_tabuleiro(tab):
    for linha in tab:
        print(' | '.join(linha))

def verificar_vitoria(tab, jogador):
    # Verificar as linhas
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True

    # Verificar as colunas
    for i in range(3):
        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True

    # Verificar diagonais 
    if (tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador) or (tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador):
        return True

    return False


tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

jogador_atual = 'X'

for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f'Jogador {jogador_atual}, escolha uma posição (1-9): ')

    # Validar entrada
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > 9:
        print("Entrada inválida. Escolha um número de 1 a 9.")
        continue

    pos = int(escolha) - 1
    linha, coluna = pos // 3, pos % 3

    if tabuleiro[linha][coluna] in ['X', 'O']:
        print('Posição já ocupada. Tente outra.')
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f'Jogador {jogador_atual} venceu!')
        break

    if jogador_atual == 'O':
        jogador_atual = 'X'
    else:
        jogador_atual = 'O'
    