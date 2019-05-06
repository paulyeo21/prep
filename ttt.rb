class TTTException < Exception
  def message
    "Not a legal move!"
  end
end

class TTTBoard
  attr_accessor :board

  def initialize
    @board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    # @is_players_turn = true
    @total_moves = 0
  end

  def to_s
    (0..2).each do |i|
      (0..2).each do |j|
        if j == 0 or j == 2
          print @board[i][j]
        else
          print "|#{@board[i][j]}|"
        end
      end
      puts
    end
  end

  def move(coordinates, token)
    raise TTTException if @total_moves > 8
    raise TTTException if @board[coordinates[0]][coordinates[1]] != "-"
    raise TTTException if (coordinates[0] > 2 and coordinates[0] < 0) or (coordinates[1] > 2 and coordinates[1] < 0)
    # token = @is_players_turn ? "X" : "O"
    @board[coordinates[0]][coordinates[1]] = token
    @total_moves += 1
  end

  def is_full?
    @total_moves == 9
  end
end

class TTTAI
  def initialize(board)
    @board = board
  end

  def move
    ai_gen_coords = generate_coordinates
    @board.move(ai_gen_coords, "O")
  end

  def generate_coordinates
    (0..2).each do |i|
      (0..2).each do |j|
        return [i, j] if @board.board[i][j] == "-"
      end
    end
  end
end

ttt = TTTBoard.new
ai = TTTAI.new(ttt)
begin
  while not ttt.is_full?
    puts "enter row coordinate: "
    row = gets
    puts "enter col coordinate: "
    col = gets
    ttt.move([row.to_i, col.to_i], "X")
    puts ttt
    ai.move
    puts ttt
  end
rescue TTTException => e
  puts "Game Over!"
end
