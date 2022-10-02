deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    current_deck = []
    half_deck = len(deck) // 2
    left_deck = deck[0: half_deck]
    right_deck = deck[half_deck:]
    for index in range(0, len(left_deck)):
        current_deck.append(left_deck[index])
        current_deck.append(right_deck[index])
    deck = current_deck
print(deck)




