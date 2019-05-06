class TTTBoard
  def initialize
    @board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    @is_players_turn = true
  end

  def move(coordinates=nil)
    token = @is_players_turn ? "X" : "O"
    if coordinates
      @board[coordinates[0]][coordinates[1]] = token
    else
      ai_gen_coords = gen_coordinates
      @board[ai_gen_coords[0]][ai_gen_coords[1]] = token
    end
    @is_players_turn = !@is_players_turn
  end

  def to_s
    (0..2).each do |i|
      (0..2).each do |j|
        if j == 0
          print @board[i][j]
        elsif j == 2
          print @board[i][j]
        else
          print "|#{@board[i][j]}|"
        end
      end
      puts
    end
  end

  def gen_coordinates
    [0,0]
  end

  def winner?
    (0..2).each do |i|
      (0..2).each do |j|
        return false if @board[i][j] == "-"
      end
    end
    winning_states = [
      [[0,0],[0,1],[0,2]],
      [[1,0],[1,1],[1,2]],
      [[2,0],[2,1],[2,2]],
      [[0,0],[1,0],[2,0]],
      [[0,1],[1,1],[2,1]],
      [[0,2],[1,2],[2,2]],
      [[0,0],[1,1],[2,2]],
      [[0,2],[1,1],[2,0]]
    ]
    winning_states.each do |state|
      coord_a, coord_b, coord_c = state
      if @board[coord_a[0]][coord_a[1]] == @board[coord_b[0]][coord_b[1]] &&
          @board[coord_a[0]][coord_a[1]] == @board[coord_c[0]][coord_c[1]] &&
          @board[coord_b[0]][coord_b[1]] == @board[coord_c[0]][coord_c[1]]
        return true
      end
    end
    return false
  end
end

ttt = TTTBoard.new
puts ttt
puts ttt.winner?
ttt.move [0,1]
puts ttt
ttt.move
puts ttt
