def floyd_warshall(adj_matrix)
  # for rows
  #   for columns
  #     for middle node
  for i..nodes
    for j..nodes
      for k..nodes
        if matrix[i, k] + matrix[k, j] < matrix[i, j]
          matrix[i, j] = matrix[i, k] + matrix[k, j] 
        end
      end
    end
  end
end
