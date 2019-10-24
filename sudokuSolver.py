import time, random

class Sudoku:
  def __init__(self, array):
    self.board=array
    self.permanent=array

  def print(self):
    for i in range(len(self.board)):
      print(self.board[i])

  def dups_in_rows(self, rowIdx):
    row=self.board[rowIdx]
    for i in range(len(row)):
      for j in range(len(row)):
        if (i!=j and row[i]==row[j]):
          return True
    return False
      
  def dups_in_cols(self, colIdx):
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        if(i!=j and self.board[i][colIdx]==self.board[j][colIdx]):
          return True
    return False

  # Removes any numbers already contained in the row from the 
  # array of possible numbers
  def is_contained_in_row(self, rowIdx, possibles):
    row=self.board[rowIdx]
    for i in range(len(row)):
      if self.board[rowIdx][i] in possibles:
        possibles.remove(self.board[rowIdx][i])

    return possibles
  # Removes any numbers already contained in the col from the 
  # array of possible numbers
  def is_contained_in_col(self, colIdx, possibles):
    for i in range(len(self.board)):
      if self.board[i][colIdx] in possibles:
        possibles.remove(self.board[i][colIdx])

    return possibles

  # Checks if 3x3 grid at starting column and starting row 
  # has duplicates
  def dups_in_box(self, row, col):
    colStart=(col//3)*3
    rowStart=(row//3)*3
    colEnd = colStart + 3
    rowEnd = rowStart + 3

    elements = []
    for colIdx in range(colStart, colEnd):
      for rowIdx in range (rowStart, rowEnd):
        if self.board[rowIdx][colIdx] in elements:
          return True
        elements.append(self.board[rowIdx][colIdx])

    return False

  # Removes items already in the box
  def is_contained_in_box(self, row, col, possibles):
    colStart=(col//3)*3
    rowStart=(row//3)*3
    colEnd = colStart + 3
    rowEnd = rowStart + 3

    for colIdx in range(colStart, colEnd):
      for rowIdx in range (rowStart, rowEnd):
        if self.board[rowIdx][colIdx] in possibles:
          possibles.remove(self.board[rowIdx][colIdx])

    return possibles


class Solution:
  def __init__(self, Sudoku):
    self.Sudoku=Sudoku
    self.solved=False
    self.frontier=[]

  def possible_sols_board(self):
    for i in range(len(self.Sudoku.board)):
      for j in range(len(self.Sudoku.board[i])):
        possibles=range(1,10)
        possibles=self.Sudoku.is_contained_in_row(i,possibles)
        possibles=self.Sudoku.is_contained_in_col(i,possibles)
        possibles=self.Sudoku.is_contained_in_box(i,j,possibles)
        self.Sudoku.board[i][j]=possibles
        print("Possibles: ", possibles)
    
  # Gets a possible soln for row,col
  def minimal(self):
    row,col,min=0,0,9
    for i in range(len(self.Sudoku.board)):
      for j in range(len(self.Sudoku.board[i])):
        if(len(self.Sudoku.board[i][j])<min):
          row,col,min=i,j,len(self.Sudoku.board[i][j])
    
    print("Minimal row and col is ", row, col)
    return row, col
  
  # Solves the Sudoku
  def solve(self):
    current=possible_sols_board()
    minrow,mincol = minimal()
    pass

  # Check if a valid solution has been found
  def is_valid(self, board):
    # Check all columns, rows, and 3x3 grids for duplicates
    for colIdx in range(9):
      if board.dups_in_cols(colIdx):
        return False 

    for rowIdx in range(9):
      if board.dups_in_rows(rowIdx):
        return False

    for rowIdx in range(9):
      for colIdx in range(9):
        if board.dups_in_box(rowIdx, colIdx):
          return False
    pass

def main():
  # easy board
  board = [[0,7,0,9,0,4,0,0,0],
            [1,0,0,7,0,2,0,9,4],
            [0,0,0,0,0,5,1,2,0],
            [0,0,0,7,8,5,2,0,0],
            [0,5,8,0,0,0,4,7,0],
            [0,0,9,4,1,6,0,0,0],
            [0,5,9,2,0,0,0,0,0],
            [2,6,0,9,0,7,0,0,5],
            [0,0,0,8,0,2,0,6,0]]

	# expert board
	# board = [
	#     [8,0,0,0,0,0,0,0,0],
	#     [0,0,3,6,0,0,0,0,0],
	#     [0,7,0,0,9,0,2,0,0],
	#     [0,5,0,0,0,7,0,0,0],
	#     [0,0,0,0,4,5,7,0,0],
	#     [0,0,0,1,0,0,0,3,0],
	#     [0,0,1,0,0,0,0,6,8],
	#     [0,0,8,5,0,0,0,1,0],
	#     [0,9,0,0,0,0,4,0,0]]


  mySudoku = Sudoku(board)
  mySudoku.print()
  start = time.time()

  soln = Solution(mySudoku)
  print( "Solved in {} seconds".format( time.time() - start ) )
  print("Final board:")
  soln.Sudoku.print()

if __name__== "__main__":
	main()
