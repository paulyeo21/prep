# Triplebyte tic tac toe
#

class TTTIllegalMove < Exception
  def message
    "Aborting program, illegal tic-tac-toe move"
  end
end

class TTTBoard
  attr_reader :board

  def initialize
    @board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
    @counter = 0
  end

  def add_token(token, coord)
    raise TTTIllegalMove if @board[coord[0]][coord[1]] == "X" or @board[coord[0]][coord[1]] == "O"
    raise TTTIllegalMove if is_full?
    @board[coord[0]][coord[1]] = token
    @counter += 1
  end

  def to_s
    (0..@board.length-1).each do |i|
      (0..@board[0].length-1).each do |j|
        if j == 0
          print "#{@board[i][j]} "
        elsif j == @board[0].length-1
          print " #{@board[i][j]}"
        else
          print "| #{@board[i][j]} |"
        end
      end
      puts
    end
  end

  def is_full?
    @counter == 9
  end
end

class TTTAI
  def initialize(board)
    @board = board.board
    @token = "O"
  end

  def move
    (0..@board.length-1).each do |i|
      (0..@board[0].length-1).each do |j|
        if @board[i][j] == "-"
          @board.add_token(@token, [i, j])
          break
        end
      end
    end
  rescue TTTIllegalMove => e
    puts e.message
  end
end

board = TTTBoard.new
ai = TTTAI.new(board)
# board.add_token("X", [0, 0]) # human move for now
# ai.move
# ai.move
puts board

