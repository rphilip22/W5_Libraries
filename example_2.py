from random import shuffle

cards = ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts',
            '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 
            'Queen of Hearts', 'King of Hearts', 'Ace of Hearts']

scards = cards.copy()
shuffle(scards)

print("\nShuffled cards:")
for card in scards:
    print(card)