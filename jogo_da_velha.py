#variavel para definir espaço em branco
branco = " "

#Lista do jogador 1 e Jogador 2
token = ["X", "O"]

#Função para criar as posições do jogo da velha 
def criar_board():
    #Matriz do jogo da velha
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]

    return board

#Função para mostrar a tabela
def print_board(board):
    for i in range(3):
        print("|".join(board[i]))

        if(i < 2):
            print('------')
#Função para verificar se o valor é válido
def get_input_valido(mensagem):
    try:
        numero = int(input(mensagem))

        if(numero >= 1 and numero <= 3):
            return numero - 1
        else:
            print("Número precisa estar entre 1 e 3")
            return get_input_valido(mensagem)
    except:
        print("Número inválido")
        return get_input_valido(mensagem)

#Função para verificar o movimento
def verifica_movimento(board, i, j):
    if(board[i][j] == branco):
        return True
    else:
        return False
#Função para fazer o movimento
def faz_movimento(board, i, j, jogador):
    board[i][j] = token[jogador]
#Função para verificar o ganhador
def verifica_ganhador(board):
    #Estrutura da linha
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
            return board[i][0]

    #Estrutura da coluna
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
            return board[0][i]

    #Estrutura da diagonal principal
    if(board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    #Estrutura da diagonal secundária
    if (board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    #Estrutura vencedor
    for i in range(3):
        for j in range(3):
            if(board[i][j] == branco):
                return False

    return "EMPATE"
