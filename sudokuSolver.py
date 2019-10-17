
def dups_in_rows:
	return True
	
def dups_in_cols:
	return True
	
def dups_in_box:
	return True


def main():
	# expert board
	board = [
	    [8,0,0,0,0,0,0,0,0],
	    [0,0,3,6,0,0,0,0,0],
	    [0,7,0,0,9,0,2,0,0],
	    [0,5,0,0,0,7,0,0,0],
	    [0,0,0,0,4,5,7,0,0],
	    [0,0,0,1,0,0,0,3,0],
	    [0,0,1,0,0,0,0,6,8],
	    [0,0,8,5,0,0,0,1,0],
	    [0,9,0,0,0,0,4,0,0]]

	print("Initial board: ", board)
	
	mySudoku = Sudoku( board )
	start = time.time()

	
	print( "Solved in {} seconds".format( time.time() - start ) )
 	


if __name__== "__main__":
	main()
