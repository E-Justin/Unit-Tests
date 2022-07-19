user_hand1 = ['Ace of spades', 'Jack of heart']
user_hand2 = ['Ace of spades', '5 of clubs']
user_hand3 = ['Ace of hearts', 'Ace of spades']
user_hand4 = ['Ace of hearts', 'Ace of spades', '8 of diamonds', 'Ace of clubs', '10 of hearts']
user_hand5 = ['Jack of clubs', '10 of diamonds', '5 of hearts']

def get_users_total(hand):
    ace_counter = 0
    # tally number of aces in hand
    for card in hand:
        if 'Ace' in card:
            ace_counter += 1

    total = 0

    for card in hand:  # iterate through cards in hand
        if 'Ace' in card:  # if the card is an ace
            total += 11  # ace == 11 (will adjust in a few lines if busts)
        elif 'Queen' in card or 'Jack' in card or 'King' in card:  # if card is a face card other than ace
            total += 10  # counts as 10
        else:  # if its a non face card
            total += int(card[0:2])  # take value of card and add to total

    while total > 21 and ace_counter > 0:  # if user busts with counting ace as 11
        total -= 10  # make ace count as 1
        ace_counter -= 1  # decrement ace counter

    return total

def test_with_two_face_cards():
    assert get_users_total(user_hand1) == 21

def test_with_one_ace():
    assert get_users_total(user_hand2) == 16

def test_with_two_aces():
    assert get_users_total(user_hand3) == 12

def test_with_two_aces_five_cards_total():
    assert get_users_total(user_hand4) == 21

def test_with_bust_three_cards():
    assert get_users_total(user_hand5) == 25
