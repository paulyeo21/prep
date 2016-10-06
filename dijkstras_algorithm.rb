require "../data-structures/priority_queue.rb"
require "../data-structures/binary_tree_node.rb"

def dijkstras_algorithm(start, goal)
  frontier = PriorityQueue.new
  frontier << [start, 0]
  cost_so_far = {}

  while not frontier.empty?
    current = frontier.pop

    if current == goal
      break
    end 

    current.neighbors.each do |neighbor|
      new_cost = cost_so_far[current] + cost(current, neighbor) 

      if not cost_so_far.include?(neighbor) or new_cost < cost_so_far[neighbor]
        frontier << [neighbor, new_cost]
      end
    end
  end
end
