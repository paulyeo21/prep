class Array
  def my_map(&block)
    self.to_enum unless block_given?
    result = []
    for i in 0..self.length - 1
      result << yield(self[i])
    end
    result 
  end
end

describe Array do 
  it "responds to my_map" do
    expect([]).to respond_to :my_map
  end

  it "returns new array" do
    expect([1, 2, 3].my_map { |x| x * 2 }).to eq([2, 4, 6])
  end
end
