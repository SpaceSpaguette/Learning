import random
from colorama import Fore

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(deck)


def print_hand(hand):
    print(Fore.WHITE, ', '.join(map(str, hand)))


def play_turn(hand):
    hand.append(deck.pop())
    print_hand(hand)
    if sum(hand) > 21:
        lives -= 1
        print(Fore.RED, f'Player has {lives} lives left.')
    if sum(hand) == 21:
        return True


def play_game():
    user_hand = [deck.pop() for _ in range(2)]
    dealer_hand = [deck.pop() for _ in range(2)]

    print_hand(user_hand)
    print_hand(dealer_hand)

    lives = 3
    while True:
        if lives == 0:
            print(Fore.RED, 'Dealer wins.')
            break
        print(Fore.WHITE, '1. Hold\n2. Take another card')
        choice = input()
        if choice == '1':
            if play_turn(user_hand):
                break
        elif choice == '2':
            if play_turn(user_hand):
                break


if __name__ == '__main__':
    play_game()
#BlackJack
import random
from colorama import Fore

#Elements for generation of deck
deck = [1,2,3,4,5,6,7,8,9,10,11]
user_hand = []
dealer_hand = []
#Shuffling
random.shuffle(deck)
usr_lives = 3
dealer_lives = 3
print(Fore.WHITE)

#User's hand
for i in range(2):
    user_hand.append(deck.pop())
print(Fore.WHITE,'User',end=" ")

for i in range(2):
    dealer_hand.append(deck.pop())
print(Fore.WHITE,'Dealer',end=" ")
while True:
    if usr_lives == 0:
        print(Fore.RED,'User has no more lives. Dealer wins.')
        break
    if dealer_lives == 0:
        print(Fore.RED,'Dealer has no more lives. User wins.')
        break

    print(Fore.WHITE, user_hand,)
    print(Fore.GREEN,1 + " Hold")
    print(Fore.WHITE, 2 + " Take another")
    userinput = input()

    if userinput == "1":
        user_hand.append(deck.pop())
        print(Fore.WHITE, user_hand)
        if sum(user_hand) > 21:
            usr_lives -= 1
            print(Fore.RED,'User has',usr_lives,'lives left.')
        if sum(user_hand) == 21:
            break
    elif userinput == "2":
        user_hand.append(deck.pop())
        print(Fore.WHITE, user_hand)
        if sum(user_hand) > 21:
            usr_lives -= 1
            print(Fore.RED,'User has',usr_lives,'lives left.')
        if sum(user_hand) == 21:
            break

#TODO refactor the whole list so it doesnt kill you when you have low hp












