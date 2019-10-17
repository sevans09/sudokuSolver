import time, random

class Sudoku:
  def __init__(self, array):
    self.board=array
    self.permanent=array

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

  # checks if 3x3 grid at starting column and starting row 
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


class Solution:
  
  # genetic crossover of non-permanent components of board
  def crossover(self, board):
    pass

  # genetic mutation of non-permanent components of board
  # mutate so that only unique numbers 1-9 are generated per 3x3
  def mutate (self, board):
    pass
  
  # calculate the fitness of current potential solution
  def determine_fitness(self, board):
    pass
  
  # check if a valid solution has been found
  def is_valid(self, board):
    # check all columns, rows, and 3x3 grids for duplicates
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


def main():
  # easy board
	board = [
	    [0,7,0,9,0,4,0,0,0],
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

	print("Initial board: ", board)
	
	mySudoku = Sudoku( board )
	start = time.time()

	
	print( "Solved in {} seconds".format( time.time() - start ) )
 	


if __name__== "__main__":
	main()
