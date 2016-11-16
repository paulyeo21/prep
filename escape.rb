require "matrix"

class Matrix
  def []=(row, column, value)
    @rows[row][column] = value
  end
end

def escape(harmful, deadly)
  # 1. get harmful regions by coordinates
  # 2. get deadly regions by coordinates
  # 3. dijkstra's algorithm to track costs to find shortest path

  adj_matrix = Matrix.build(500, 500) {|r, c| 0}

  for region in harmful
    region = region.split(" ")
    (region[0]..region[2]).each do |x|
      (region[1]..region[3]).each do |y|
        adj_matrix[x, y] = 1
      end
    end
  end

  for region in deadly
    region = region.split(" ")
    (region[0]..region[2]).each do |x|
      (region[1]..region[3]).each do |y|
        adj_matrix[x, y] = nil
      end
    end
  end
 
  frontier = PriorityQueue.new
  frontier.push([0, 0], 0) 

  while not frontier.emtpy?
    current, cost = frontier.pop
    
    if current[0] == 500 and current[1] == 500
      break
    end

    next if current[0] < 0 or current[0] > 500 or current[1] < 0 or current[1] > 500
    next if adj_matrix[current[0], current[1]].nil?

    # Check x+-1 y+-1 neighbors
    # if not in deadly region
    # if inside harmful region then cost += 1
    (-1..1).each do |x|
      neighbor = [current[0] + x, current[1]]
      new_cost = adj_matrix[neighbor[0], neighbor[1]] + cost
      if new_cost < cost_so_far[neighbor] or not cost_so_far.include?(neighbor)
        cost_so_far[neighbor] = new_cost
        frontier.push(neighbor, new_cost)
        came_from[neighbor] = current
      end
    end

    (-1..1).each do |y|
      neighbor = [current[0], current[1] + y]
      new_cost = adj_matrix[neighbor[0], neighbor[1]] + cost
      if new_cost < cost_so_far[neighbor] or not cost_so_far.include?(neighbor)
        cost_so_far[neighbor] = new_cost
        frontier.push(neighbor, new_cost)
        came_from[neighbor] = current
      end
    end
  end

  return came_from
end
