require_relative "credit_card_provider"
require_relative "credit_card"

def valid_card
  provider = CreditCardProvider.new

  # Test card validation using Luhn 10
  valid_card = CreditCard.new(name: "Tom", number: "4111111111111111", limit: "$1000")
  puts "Test credit card is valid: #{valid_card.valid? == true}"

  # Test balance summary after adding valid card
  provider.add(valid_card)
  puts "Test summary after adding Tom's card: #{provider.summary == "Tom: $0\n"}"
end

def invalid_card
  provider = CreditCardProvider.new

  # Test card validation using Luhn 10
  invalid_card = CreditCard.new(name: "Quincy", number: "1234567890123456", limit: "$2000")
  puts "Test credit card is invalid: #{invalid_card.valid? == false}"

  # Test balance summary after adding invalid card
  provider.add(invalid_card)
  puts "Test summary after adding invalid card: #{provider.summary == "Quincy: error\n"}"
end

def valid_and_invalid_cards
  provider = CreditCardProvider.new
  valid_card = CreditCard.new(name: "Tom", number: 4111111111111111, limit: "$1000")
  invalid_card = CreditCard.new(name: "Quincy", number: 1234567890123456, limit: "$2000")
  provider.add(valid_card)
  provider.add(invalid_card)

  # Test balance summary includes both valid and invalid cards and they are in alphabetical order
  puts "Test summary after adding valid and invalid cards: #{provider.summary == "Quincy: error\nTom: $0\n"}"
end

def charges
  provider = CreditCardProvider.new
  valid_card = CreditCard.new(name: "Tom", number: 4111111111111111, limit: "$1000")
  provider.add(valid_card)

  # Test balance increase of card after charging
  tom = provider.card_of("Tom")
  tom.charge("$500")
  puts "Test credit card balance: #{tom.balance == 500}"

  # Test single charge
  puts "Test single charge of credit card: #{provider.summary == "Tom: $500\n"}"

  # Test multiple charges
  tom.charge("$500")
  puts "Test multiple charges credit card: #{provider.summary == "Tom: $1000\n"}"

  # Test charges over card limit
  tom.charge("$300")
  puts "Test charges over card limit: #{provider.summary == "Tom: $1000\n"}"
end

def credits
  provider = CreditCardProvider.new
  valid_card = CreditCard.new(name: "Lisa", number: 5454545454545454, limit: "$3000")
  provider.add(valid_card)

  # Test balance decreases of card after credit
  lisa = provider.card_of("Lisa")
  lisa.credit("$100")
  puts "Test credit card balance after credit: #{lisa.balance == -100}"

  # Test charging after crediting a card
  lisa.charge("$7")
  puts "Test credit card balance after charge: #{lisa.balance == -93}"

  # Test summary returns negative balance
  puts "Test summary after credit and charge: #{provider.summary == "Lisa: $-93\n"}"
end

valid_card()
invalid_card()
valid_and_invalid_cards()
charges()
credits()

