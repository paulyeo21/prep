class CreditCard
  attr_reader :number, :name, :limit, :balance

  def initialize(name:, number:, limit:)
    @name = name
    @number = number
    @limit = sanitize(limit)
    @balance = 0
  end

  def valid?
    name and number and limit and luhn_checksum == 0
  end

  # If card exists and balance is not surpassed update balance otherwise ignore
  def charge(amount)
    amount = sanitize(amount)
    @balance += amount if @limit >= @balance + amount
  end

  def credit(amount)
    @balance -= sanitize(amount)
  end

  private

  ### https://en.wikipedia.org/wiki/Luhn_algorithm
  def digits_of(number)
    digits = number.to_s.chars
    digits.map { |i| i.to_i }
  end

  def luhn_checksum
    digits = digits_of(number)
    odd = digits.select.each_with_index {|d, i| i.odd?}
    even = digits.select.each_with_index {|d, i| i.even?}
    total = odd.inject(:+)
    for num in even
      total += digits_of(2 * num).inject(:+)
    end
    total % 10
  end
  ###

  # i.e "$100" to 100
  def sanitize(amount)
    amount.sub("$", "").to_i if amount
  end
end
