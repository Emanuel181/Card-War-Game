import validations
import player_class
import deck_class

def start():
    deck = deck_class.Deck()

    print('\n\t\t\t\t\t  Enter name of player 1: ', end=' ')
    name1 = validations.validation_for_name()
    while not name1:
        print(
            '\n\t\t\t\t\t  A valid name must have minimum 3 characters, contain only letters from alphabet and a space between names!')
        print('\n\t\t\t\t\t  Enter name of player 1: ', end=' ')
        name1 = validations.validation_for_name()

    print('\n\t\t\t\t\t  Enter name of player 2: ', end=' ')
    name2 = validations.validation_for_name()
    while not name2 or name2 == name1:
        print(
            '\n\t\t\t\t\t  A valid name must be unique, has minimum 3 characters, contain only letters from alphabet and a space between names!')
        print('\n\t\t\t\t\t  Enter name of player 2: ', end=' ')
        name2 = validations.validation_for_name()

    player_1 = player_class.Player(deck.card_list[:(len(deck.card_list) // 2) + 1:], name1)
    player_2 = player_class.Player(deck.card_list[(len(deck.card_list) // 2) + 1:], name2)

    round, round_list = 1, []

    while True:
        round_list.append(player_1.extract_card())
        round_list.append(player_2.extract_card())

        print(f'\n\n\t\t\t\t   ┍━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┑\
                    \n\t\t\t\t\t\t\t     Round: {round}')
        print(f'\n\t\t\t\t\t\t\t{name1} has {round_list[-2].value} of {round_list[-2].suit}')
        print(f'\n\t\t\t\t\t\t\t{name2} has {round_list[-1].value} of {round_list[-1].suit}')
        print('\n\t\t\t\t   ┕━━━━━━━━━━━━━━━━━━♔━━━━━━━━━━━━━━━━━━┙')

        if round_list[-2].value > round_list[-1].value and player_2.cards_left() == 0:
            print(f'\n\t\tPlayer »»———— {player_1.name} ————-«« won, player {player_2.name} has 0 cards left.\n')
            del round_list
            return

        elif round_list[-2].value > round_list[-1].value:
            print(f'\n\t\t\t\tWho won this round: Player {player_1.name} won {len(round_list)} cards!')
            player_1.win_cards(round_list)
            round_list.clear()

        elif round_list[-2].value < round_list[-1].value and player_1.cards_left() == 0:
            print(f'\n\t\tPlayer »»———— {player_2.name} ————-«« won, player {player_1.name} has 0 cards left.\n')
            del round_list
            return

        elif round_list[-2].value < round_list[-1].value:
            print(f'\n\t\t\t\tWho won this round: Player {player_2.name} won {len(round_list)} cards!')
            player_2.win_cards(round_list)
            round_list.clear()

        else:
            print(f'\n\t\t\t\t\t\t\t  [WAR at round {round}]')

            if player_1.cards_left() < 5:
                print(f'\n\t\tPlayer »»———— {player_2.name} ————-«« won, player {player_1.name} has less then 5 cards left.\n')
                del round_list
                return

            if player_2.cards_left() < 5:
                print(f'\n\t\tPlayer »»———— {player_1.name} ————-«« won, player {player_2.name} has 0 cards left.\n')
                del round_list
                return

            for _ in range(5):
                round_list.append(player_1.extract_card())
            for _ in range(5):
                round_list.append(player_2.extract_card())
            del _

            if player_1.cards_left() == 0:
                print(f'\n\t\tPlayer »»———— {player_2.name} ————-«« won, player {player_1.name} has 0 cards left.\n')
                del round_list
                return

            if player_2.cards_left() == 0:
                print(f'\n\\ttPlayer »»———— {player_2.name} ————-«« won, player {player_2.name} has 0 cards left.\n')
                del round_list
                return

        round += 1
