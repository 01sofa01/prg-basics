def f(player1, player2):
    letters = {
        "2" : 2,
        "3" : 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q":12,
        "K":13,
        "A": 14
    
    }
    card1 = 0
    card2 = 0
    for card_number in range (len(player1)):
        card1 += letters[player1[card_number]]
    while len(player2) > 0:
        card2 += letters[player2[0]]
        player2 = player2[1:]
    if card1 >= card2:
        return True
    else:
        return False 
def main():
   card = "QK245"
   card2 = "J9987"
   print(f(card, card2))
   print(f(card, "J9987"))

if __name__ == "__main__":
    main()
    
