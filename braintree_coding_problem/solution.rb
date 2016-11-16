require_relative "credit_card_provider"
require_relative "credit_card"

provider = CreditCardProvider.new
ARGF.each do |line|
  arguments = line.split(" ")

  case arguments[0].downcase
  when "add"
    card = CreditCard.new(name: arguments[1], number: arguments[2], limit: arguments[3])
    provider.add(card)
  when "charge"
    card = provider.card_of(arguments[1])
    card.charge(arguments[2]) if card
  when "credit"
    card = provider.card_of(arguments[1])
    card.credit(arguments[2]) if card
  end
end

puts provider.summary
