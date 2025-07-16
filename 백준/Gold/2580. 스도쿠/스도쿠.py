import sys
input=sys.stdin.readline

board=[list(map(int,input().split())) for _ in range(9)]

blankList=[]
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            blankList.append((i,j))

def check(pos,num):
    for i in range(9):
        if board[pos[0]][i]==num:
            return False
    for i in range(9):
        if board[i][pos[1]]==num:
            return False
    for i in range(pos[0]//3*3,pos[0]//3*3+3):
        for j in range(pos[1]//3*3,pos[1]//3*3+3):
            if board[i][j]==num:
                return False
    return True
    
def dfs(deep,board):
    global blankList
    if deep==len(blankList):
        for i in range(9):
            print(*board[i])
        return True
    for i in range(1,10):
        if check(blankList[deep],i):
            board[blankList[deep][0]][blankList[deep][1]]=i
            if dfs(deep+1,board):
                return True
            board[blankList[deep][0]][blankList[deep][1]]=0
    return

dfs(0,board)