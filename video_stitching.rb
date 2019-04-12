# 1024. Video Stitching
#
# You are given a series of video clips from a sporting event that lasted T seconds.
# These video clips can be overlapping with each other and have varied lengths.
#
# Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at 
# time clips[i][1].  We can cut these clips into segments freely: for example, a clip 
# [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
#
# Return the minimum number of clips needed so that we can cut the clips into segments 
# that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.

# Sort the list by x, then greedily find clips that increase the range.
# T: O(n)
# S: O(1)
def video_stitching(clips, t)
  # puts clips.sort.inspect
  clips.sort!
  output, stitched, candidate = 0, [0,0], clips[0]
  return -1 if candidate[0] != 0
  clips[1..-1].each do |current|
    if current[0] > stitched[1]
      if candidate[1] >= t
        break
      else
        stitched = candidate
        candidate = current
        output += 1
      end
    elsif current[0] <= stitched[1] and current[1] > candidate[1]
      candidate = current
    end
  end
  if candidate
    stitched = candidate
    output += 1
  end
  return stitched[1] >= t ? output : -1
end

puts video_stitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10) #3
puts video_stitching([[0,1],[1,2]], 5) #-1
puts video_stitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9) #3
puts video_stitching([[0,4],[2,8]], 5) #2
puts video_stitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]], 5) #1
puts video_stitching([[3,12],[7,14],[9,14],[12,15],[0,9],[4,14],[2,7],[1,11]], 10) #2
puts video_stitching([[24,28],[10,56],[50,78],[38,77],[38,78],[3,69],[33,49],[66,89],[73,83],[6,12],[24,86],[67,82],[18,26],[1,57],[13,30],[8,56],[58,78],[2,84],[35,39],[45,51],[30,32],[19,31],[32,70],[1,15],[16,18],[32,87],[32,87],[39,42],[81,84],[25,61],[26,34],[10,82],[17,34],[56,72],[17,22],[8,83],[5,21],[3,79],[12,73],[0,28],[74,76],[41,79],[4,60],[51,90],[10,41],[47,90],[44,56],[13,16],[43,83],[0,22],[30,40],[8,27],[57,58],[0,26],[16,66],[62,89],[2,74],[17,61],[25,28],[23,54],[42,79],[14,28],[26,77],[34,36],[17,42],[72,81],[12,87],[3,57],[81,88],[65,87],[35,74],[19,77],[10,53],[38,75],[14,90],[10,90],[57,62],[37,74],[24,80],[52,63],[52,55],[64,73],[45,79],[12,19],[26,38],[40,81],[28,48],[33,62],[18,50],[9,40]], 72) #2
