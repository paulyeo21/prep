class CreditCardProvider
  def initialize
    @cards = {}
  end

  # Add key value pair of card holder name to card object to dict
  # but if card does not pass Luhn 10 then value of key value pair will be nil
  def add(card)
    card.valid? ? @cards[card.name] = card : @cards[card.name] = nil
  end

  # Generate summary with card holder's name and balance in alphabetical order
  def summary
    output = ""
    for name in @cards.keys.sort
      balance = (@cards[name] ? "$#{balance_of(name)}" : "error")
      output += "#{name}: #{balance}\n"
    end
    output
  end
  
  def card_of(name)
    @cards[name]
  end

  private

  def balance_of(name)
    @cards[name].balance
  end
end
