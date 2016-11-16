def is_balanced_bst_iterative(root)
  queue = Queue.new
  queue.push([root, max, min])

  while not queue.empty?
    current, max, min = queue.pop

    if current.value > max || current.value < min
      return false
    end

    if current.left
      queue.push(current.left, current.value, min)
    end

    if current.right
      queue.push(current.right, min, current.value)
    end
  end

  return true
end

def is_balanced_bst_recursive(root)
  if not root
    return true
  end

  if current.value > max || current.value < min
    return false
  end 

  return is_balanced_bst_recursive(root.left) \
    and is_balanced_bst_recursive(root.right)
end
