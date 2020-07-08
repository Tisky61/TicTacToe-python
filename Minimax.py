from copy import deepcopy
class TicTacToe:
    def __init__(self):
        self.tabuleiro = [0,0,0],[0,0,0],[0,0,0]
        self.turno = True
    def play(self,x,y):
        if(self.tabuleiro[x][y]):
                return False
        self.tabuleiro[x][y] = int(int(self.turno)+1)
        self.turno = not(deepcopy(self.turno))
        return True
    def copy(self,newtab):
        self.tabuleiro = deepcopy(newtab.tabuleiro)
        self.turno = deepcopy(newtab.turno)
    def AllValidPlays(self):
	    orig = self
	    output = []
	    for x in range(3):
	        for y in range(3):
	            if(self.tabuleiro[x][y]==0):
	                novo_tab = TicTacToe()
	                novo_tab.copy(orig)
	                novo_tab.play(x,y)
	                output.append(novo_tab)
	    return output
    def Evaluate(self):
        for x in range(3):
            if(self.tabuleiro[x][0]!=0 and self.tabuleiro[x][0]==self.tabuleiro[x][1]==self.tabuleiro[x][2]):
                return self.tabuleiro[x][0]
        for x in range(3):
            if(self.tabuleiro[0][x]!=0 and self.tabuleiro[0][x]==self.tabuleiro[1][x]==self.tabuleiro[2][x]):
                return self.tabuleiro[0][x]
        if(self.tabuleiro[0][0]!= 0 and self.tabuleiro[0][0]==self.tabuleiro[1][1]==self.tabuleiro[2][2]):
            return self.tabuleiro[0][0]
        if(self.tabuleiro[1][1]!= 0 and self.tabuleiro[2][0]==self.tabuleiro[1][1]==self.tabuleiro[0][2]):
            return self.tabuleiro[1][1]
        for x in range(3):
            for y in range(3):
                if(not(self.tabuleiro[x][y])):
                    return 0
        return 3
    def PrintBoard(self):
        for x in range(3):
            output = []
            for y in range(3):
                tab = [" ","O","X"]
                output += tab[self.tabuleiro[y][x]]
            print(output)
        resultados = ["Nao decidido","Vitoria da bola!","Vitoria da Cruz!","Empate!"]
        print(resultados[self.Evaluate()])
        return self.Evaluate()
def minimax(node,depth,maximazingplayer):
    if(node.Evaluate()):
        ScoreTable = [0,1,-1,0]
        return ScoreTable[node.Evaluate()]
    if(maximazingplayer):
        value = -9999999999999999999
        for x in node.AllValidPlays():
            value = max(value,minimax(x,depth-1,False))
        return value
    else:
        value =  9999999999999999999
        for x in node.AllValidPlays():
            value = min(value,minimax(x,depth-1,True))
        return value
def Play(board):
    value = -9999999999999999999
    best_board = board
    for x in board.AllValidPlays():
        temp = minimax(x,0,False)
        if(temp>value):
            value = temp
            best_board = deepcopy(x)
    return best_board
c = TicTacToe()
c.PrintBoard()
while(True):
	while(not(c.play(int(input("Digite X:")),int(input("Digite Y:"))))):
		print("Jogada Invalida!!!")
		c.PrintBoard()
	if(c.PrintBoard()):
		print("Fim de jogo!")
		break
	print("Processando IA:")
	c = Play(c)
	if(c.PrintBoard()):
		print("Fim de jogo!")
		break
input()
