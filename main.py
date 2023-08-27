import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
card_num = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    card = random.choice(card_num)
    return card


def calc_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    # Checks if ace (with value 11) is in cards and if the sum is greater than 21
    if 11 in cards and sum(cards) > 21:
        # Changes the value of ace from 11 to 1
        cards.insert(cards.index(11), 1)
        cards.remove(11)
    return sum(cards)


def result(user_score, computer_score):
    """Takes the user's and computer's scores and returns the result of the game"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def display_cards(card_list):
    """Will take either a single card or a list of cards. Returns the name of the card."""
    if type(card_list) == list:
        names = []
        # If the argument is a list of cards, then iterates through all the cards
        for card in card_list:
            # Checks for the value of 11 or 1 and identifies the card as 'ace'
            if card == 11 or card == 1:
                names.append("A")
            # If the card has a value of 10, it chooses a random card from 10, jack, queen and king
            elif card == 10:
                names.append(random.choice([10, "J", "Q", "K"]))
            # Otherwise, the card is a number card
            else:
                names.append(card)
    else:
        # If the argument is a single card, checks the conditions for that card
        if card_list == 11 or card_list == 1:
            names = "A"
        elif card_list == 10:
            names = random.choice([10, "J", "Q", "K"])
        else:
            names = card_list
    return names


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # deals 2 cards to both the computer and the user
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Identifies the name of the computer's first card and stores it
    computer_first_card = display_cards(computer_cards[0])
    user_cards_names = display_cards(user_cards)
    while not is_game_over:
        # Calculates user and computer's current score
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        # Prints the user's hand and the computer's first card, along with the user's score
        print(f"   Your cards: {user_cards_names}, current score: {user_score}")
        print(f"   Computer's first card: {computer_first_card}")
        # If anyone has a score of 21, it's a blackjack and the game ends
        if user_score == 21 or computer_score == 21 or user_score > 21:
            is_game_over = True
        else:
            # Otherwise continues the game and asks if the user wants to hit or stand
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                # If the user wants another card, it gets a random card and adds it to the card lists
                cur_card = deal_card()
                user_cards.append(cur_card)
                user_cards_names.append(display_cards(cur_card))
            else:
                # If the user chooses to pass, the game ends
                is_game_over = True

    # while the computer's score is less than 17 and the user's score is not greater than 21, it continues dealing
    # cards to the computer
    while user_score <= 21 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    # Displays final result of the game along with the hands and scores
    print(f"   Your final hand: {user_cards_names}, final score: {user_score}")
    print(f"   Computer's final hand: {[computer_first_card] + display_cards(computer_cards[1:])}, final score:"
          f" {computer_score}")
    print(result(user_score, computer_score))


# Asks the user if they want to play another game, if not, ends the program
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
