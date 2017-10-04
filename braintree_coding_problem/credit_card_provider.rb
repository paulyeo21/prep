class CreditCardProvider
  # Class stores Card objects and spits out summary
  # Assumptions:
  #   Card class has methods: "valid?" "name" "balance"
  #
  def initialize
    # Better to have a sorted hash map
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

  # Assume Card oject has "balance" method
  def balance_of(name)
    @cards[name].balance
  end
end
