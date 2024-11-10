import random

# Deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def adjust_for_ace(cards):
    """Adjust the score by converting Aces (11) to 1 if the total score exceeds 21."""
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return cards


def get_final_computer_cards(current_cards):
    """Ensure the computer's cards meet the Blackjack rules."""
    while sum(current_cards) < 17:
        current_cards.append(random.choice(cards))
        current_cards = adjust_for_ace(current_cards)
    return current_cards


def run_blackjack():
    """Main function to play Blackjack."""
    print("\n" * 5)  # Clear screen for a clean start

    # Initialize user and computer cards
    user_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)
    user_cards = adjust_for_ace(user_cards)
    computer_cards = adjust_for_ace(computer_cards)
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    # Check for Blackjack
    if computer_score == 21:
        print("You lose. The computer has Blackjack!")
        return
    elif user_score == 21:
        print("You win with a Blackjack!")
        return

    # User's turn
    while True:
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
        if user_choice == 'y':
            user_cards.append(random.choice(cards))
            user_cards = adjust_for_ace(user_cards)
            user_score = sum(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")

            if user_score > 21:
                print(f"    Your final hand: {user_cards}, final score: {user_score}")
                print("You went over. You lose 😭")
                return
        elif user_choice == 'n':
            break
        else:
            print("Invalid input! Please type 'y' or 'n'.")
    # Computer's turn
    computer_cards = get_final_computer_cards(computer_cards)
    computer_score = sum(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Determine the winner
    if computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score == computer_score:
        print("It's a draw!")
    elif user_score > computer_score:
        print("You win 😁")
    else:
        print("You lose 😭")


# Run the game in a loop for replay functionality
while True:
    run_blackjack()
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break