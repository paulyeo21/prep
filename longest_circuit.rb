require "../data-structures/priority_queue.rb"
require "matrix"

class Matrix
  def []=(row, column, value)
    @rows[row][column] = value
  end
end

def longest_circuit(connects, costs)
  # 1. Build adjacency matrix
  # 2. Run dijkstra's for each node to finding longest circuit

  n = connects.length
  adj = Matrix.build(n, n) {|r, c| 0}
  (0..n-1).each do |i|
    neighbors = connects[i].split(" ")
    cost = costs[i].split(" ")

    (0..neighbors.length-1).each do |j|
      adj[i, neighbors[j].to_i] = cost[j]
    end
  end

  longest_circuit = 0
  output = {}
  (0..n-1).each do |v|
    frontier = PriorityQueue.new
    cost_so_far = {}
    came_from = {}  
    frontier << [v, 0]

    while not frontier.empty?
      current, cost = frontier.pop
      
      (0..n-1).each do |w|
        if v != w
          new_cost = cost + adj[v, w].to_i
          
          if new_cost < cost_so_far[w].to_i or not cost_so_far.include?(w)
            cost_so_far[w] = new_cost
            frontier << [w, new_cost]
            came_from[w] = v
          end
        end
      end
    end

    current_circuit_cost = 0
    current = v
    while current
      current_circuit_cost += cost_so_far[current]
      current = came_from[v] 
    end

    if longest_circuit < current_circuit_cost
      longest_circuit = current_circuit_cost
      output = came_from
    end
  end

  output
end

connects = ["1 2", "2", ""]
costs = ["5 3", "7", ""]
puts longest_circuit(connects, costs)
