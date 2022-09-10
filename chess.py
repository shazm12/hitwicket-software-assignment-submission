# Written By: Shamik Bera
# Date : 2019-10-19
# Code for Chess game
import time 
import sys
# Board is a 5x5 matrix
board = [['-' for i in range(5)] for i in range(5)]

# class for Pawn Piece
class Pawn:
    def __init__(self,id,team,pos, type, killable=False):
        self.id = id
        self.team = team
        self.type = type
        self.killable = killable
        self.pos = pos
    
    # Function to check if the move is valid or not
    def valid_move(self,move):
        if(move=='F'):
            if self.team== 'A' and self.pos[0] -1>= 0:
                return True
            elif self.team== 'B' and self.pos[0]+1 <= 4:
                return True
            else:
                return False
        if(move=='B'):
            if self.team== 'A' and self.pos[0] + 1 <= 4:
                return True
            elif self.team== "B" and self.pos[0]- 1>= 0:
                return True
            else:
                return False
        if(move=='L'):
            if self.team== 'A' and self.pos[1] - 1 >= 0:
                return True
            elif self.team== 'B' and self.pos[1]+ 1 <= 4:
                return True
            else:
                return False
        if(move=='R'):
            if self.team== 'A' and self.pos[1] + 1 <= 4:
                return True
            elif self.team== 'B' and self.pos[1] - 1 >= 0:
                return True
            else:
                return False
 
# Function to print the board        
def print_board():
    for i in range(5):
        for j in range(5):
            print(board[i][j], end=' ')
        print()

# Function to intialize the player 1
def intializeP1(*args):
    for i in range(len(args)):
        board[4][i] = 'A-P'+args[i].id
        args[i].pos = [4,i]    
        
# Function to intialize the player 2
def intializeP2(*args):
    for i in range(len(args)):
        board[0][i] = 'B-P'+args[i].id
        args[i].pos = [0,i] 
         
# Function to make move for player 1
def make_move_1(move,obj,*obj2):
    if(obj.valid_move(move)):
        if(move=='F'):
            if(board[obj.pos[0]-1][obj.pos[1]] != '-'):
                p2 = board[obj.pos[0]][obj.pos[1]]
                p2Obj = [item for item in obj2 if item.id == p2[3]][0]
                obj2.remove(p2Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id   
                            
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]-1][obj.pos[1]] = obj.team+'-P'+obj.id
            obj.pos[0] -= 1
         
        if(move=='B'):
            if(board[obj.pos[0]+1][obj.pos[1]] != '-'):
                p2 = board[obj.pos[0]][obj.pos[1]]
                p2Obj = [item for item in obj2 if item.id == p2[3]][0]
                obj2.remove(p2Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id   
                            
                    
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]+1][obj.pos[1]] = obj.team+'-P'+obj.id
            obj.pos[0] += 1
        
        if(move=='L'):
            if(board[obj.pos[0]][obj.pos[1]-1] != '-'):
                p2 = board[obj.pos[0]][obj.pos[1]]
                p2Obj = [item for item in obj2 if item.id == p2[3]][0]
                obj2.remove(p2Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id   
                            
            
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]][obj.pos[1]-1] = obj.team+'-P'+obj.id
            obj.pos[1] -= 1
        
        if(move=='R'):
            if(board[obj.pos[0]][obj.pos[1]+1] != '-'):
                p2 = board[obj.pos[0]][obj.pos[1]]
                p2Obj = [item for item in obj2 if item.id == p2[3]][0]
                obj2.remove(p2Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id   
                            
            
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]][obj.pos[1]+1] = obj.team+'-P'+obj.id
            obj.pos[1] += 1
    else:
        print("Invalid Move")
        sys.exit(0)
 
# Function to make move for player 2 
def make_move_2(move,obj,*obj1):
    if(obj.valid_move(move)):
        if(move=='F'):
            if(board[obj.pos[0]+1][obj.pos[1]] != '-'):
                p1 = board[obj.pos[0]][obj.pos[1]]
                p1Obj = [item for item in obj1 if item.id == p1[3]][0]
                obj1.remove(p1Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id
        
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]+1][obj.pos[1]] = obj.team+'-P'+obj.id
            obj.pos[0] += 1
        
        if(move=='B'):
            if(board[obj.pos[0]-1][obj.pos[1]] != '-'):
                p1 = board[obj.pos[0]][obj.pos[1]]
                p1Obj = [item for item in obj1 if item.id == p1[3]][0]
                obj1.remove(p1Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id
        
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]-1][obj.pos[1]] = obj.team+'-P'+obj.id
            obj.pos[0] -= 1       
        if(move=='L'):
            if(board[obj.pos[0]][obj.pos[1]+1] != '-'):
                p1 = board[obj.pos[0]][obj.pos[1]]
                p1Obj = [item for item in obj1 if item.id == p1[3]][0]
                obj1.remove(p1Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id
        
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]][obj.pos[1]+1] = obj.team+'-P'+obj.id
            obj.pos[1] += 1

        if(move=='R'):
            if(board[obj.pos[0]][obj.pos[1]-1] != '-'):
                p1 = board[obj.pos[0]][obj.pos[1]]
                p1Obj = [item for item in obj1 if item.id == p1[3]][0]
                obj1.remove(p1Obj)
                board[obj.pos[0]][obj.pos[1]] = obj.team+'-P'+obj.id
        
            board[obj.pos[0]][obj.pos[1]] = '-'
            board[obj.pos[0]][obj.pos[1]-1] = obj.team+'-P'+obj.id
            obj.pos[1] -= 1

                
    else:
        print("Invalid Move")
        sys.exit(0)
 
# Driver code
if __name__ == "__main__":
    print_board()
    p1 =  [item for item in  input("Enter Pieces for Player 1: ").split(",")]
    if(len(p1) > 5):
        print("Invalid input")
        sys.exit()
    p2 =  [item for item in  input("Enter Pieces for Player 2: ").split(",")]
    if(len(p2) > 5):
        print("Invalid input")
        sys.exit()
    p1Obj = [Pawn(item[1],"A",[0,0], "Pawn") for item in p1]
    p2Obj = [Pawn(item[1],"B",[0,0], "Pawn") for item in p2]
    intializeP1(*p1Obj)
    intializeP2(*p2Obj)
    print_board()
    while(True):
        p1move = input("Enter move for Player 1: ").split(":")
        obj1 = [item for item in p1Obj if item.id == p1move[0][1]][0]
        index1 = p1Obj.index(obj1)
        make_move_1(p1move[1],p1Obj[index1],p2Obj)
        print_board()
        p2move = input("Enter move for Player 2: ").split(":")
        obj2 = [item for item in p2Obj if item.id == p2move[0][1]][0]
        index2 = p2Obj.index(obj2)
        make_move_2(p2move[1],p2Obj[index2],p1Obj)
        print_board()
        # Check if any player has won by checking length of the player''s pawn pieces object list
        if(len(p1Obj) == 0):
            print("Player 2 wins")
            break
        elif (len(p2Obj) ==0):
            print("Player 1 wins")
            break
    
