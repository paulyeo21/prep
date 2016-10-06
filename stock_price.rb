def stock_price(stocks)
  cheapest = stocks[0]
  profit = stocks[1] - stocks[0] 
  for stock in stocks[1..-1]
    if stock - cheapest > profit
      profit = stock - cheapest
    end

    cheapest = stock if stock < cheapest
  end
  return profit
end

stocks = [10, 7, 5, 8, 11, 9]
stocks1 = [-1, 3, 5, -2, 4, 10]
stocks2 = [0, -5, -6, -7, -8, -9]
puts stock_price(stocks)
puts stock_price(stocks1)
puts stock_price(stocks2)
