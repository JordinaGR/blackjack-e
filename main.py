import random, time

class Deck:
    
    deck = []
    letter_cards_values = {'A':11, 'J':10, 'Q':10, 'K':10}
    letter_cards = ['A', 'J', 'Q', 'K']

    def generate_decks(self, numdecks):
        while numdecks > 0:

            for i in range(2, 11):
                self.deck.append(i)

            self.deck += self.letter_cards

            numdecks -= 1

        return self.deck

    def print_deck(self):
        print(self.deck)

    def gen_two_cards(self):
        random.shuffle(self.deck)

        c1 = self.deck.pop()
        c2 = self.deck.pop()
        pc1 = self.deck.pop()
        pc2 = self.deck.pop()

        return c1, c2, pc1, pc2

    def get_one_card(self):
        random.shuffle(self.deck)

        ec = self.deck.pop()

        return ec

    def add_cards(self, d1, d2):
        if type(d1) == int and type(d2) == int:
            return d1 + d2

        else:
            if type(d1) == str and type(d2) == str:
                d1 = self.letter_cards_values[d1]
                d2 = self.letter_cards_values[d2]
            
            elif type(d1) == str and type(d2) == int:
                d1 = self.letter_cards_values[d1]

            elif type(d1) == int and type(d2) == str:
                d2 = self.letter_cards_values[d2]

            return d1 + d2

    def start_play(self, wclass, money):
        classdeck = Deck()
        classgamerandom = GameRandom()
        classgamedif = GameDif()

        if len(self.deck) <= 10:
            print("\nNot enought cards, the match is over\n")
            main()

        print('________________________________________________________________________________')

        if money == 0:
            print("You don't have enough money\n")
            main()

        bet = int(input(f'\nYou have {money} how much do you bet? '))

        if bet > money:
            print("Not enough money\n")
            self.start_play('r', self.money)

        c1, c2, pc1, pc2 = self.gen_two_cards()

        print(f"\nYour cards are: {c1} and {c2} ")

        print(f"Computer cards are: {pc1} and {'?'}")

        result_player = self.add_cards(c1, c2)
        result_comp = self.add_cards(pc1, pc2)

        if wclass == 'r':
            classgamerandom.rounds(result_player, result_comp, True, True, pc1, pc2, bet)

        elif wclass == 'd':
            classgamedif.round()

class GameRandom(Deck):

    money = 5000

    def rounds(self, result_player, result_comp, possible, possiblec, pc1, pc2, bet):
        
        while possible is True:
            if result_player > 21:
                print(f'You lost! {result_comp} to {result_player}')
                self.money -= bet
                super().start_play('r', self.money)

            elif result_player == 21:
                print('Blackjack, you win')
                self.money = (self.money + bet) + (bet/2)
                super().start_play('r', self.money)

            morecard = str(input("\nDo you want another card? (y/n) "))

            if morecard.lower() == 'y':
                tmp = super().get_one_card()
                result_player = super().add_cards(result_player, tmp)
                print(tmp)
                time.sleep(2)

            elif morecard.lower() == 'n':
                print('You got a ', result_player)
                time.sleep(2)
                possible = False

        print(f"\nComputer had {pc1} and {pc2}")
        time.sleep(2)

        while possiblec is True:
            if result_comp > 21:
                print(f'You win! {result_comp} to {result_player}')
                self.money += bet
                super().start_play('r', self.money)
            elif result_comp == 21:
                print('Blackjack, comp win')
                self.money = (self.money - bet) - (bet/2)
                super().start_play('r', self.money)

            if result_comp < 17:
                tmp = super().get_one_card()
                print(f"\nComputer took {tmp}")
                time.sleep(2)
                result_comp = super().add_cards(result_comp, tmp)

            elif result_comp >= 17:
                print('\nThe computer does not take a card')
                time.sleep(2)
                possiblec = False

        if result_comp == result_player:
            print(f"\nIt was a draw {result_comp} to {result_player}")
            self.money -= bet

        if result_comp > result_player:
            print(f"\nThe computer won {result_comp} to {result_player} ")
            self.money -= bet

        if result_comp < result_player:
            print(f"\nYou won {result_player} to {result_comp} ")
            self.money += bet

        super().start_play('r', self.money)

    def main_random(self):
        super().start_play('r', self.money)

class GameDif(Deck):

    money = 1000

    def round(self):
        print('correcte')

    def play_dif(self):
        super().start_play('d', self.money)

class GameImp(Deck):
    pass

def main():
    print("LET'S PLAY BLACKJACK")
    version_selected = str(input('Do you wanna play the random version (r), the dificult (d) or impossible (i) '))
    number_decks = int(input('How many decks do you wanna play with? ' ))
    classdeck = Deck()

    if version_selected.lower() == 'r':
        classdeck.generate_decks(number_decks)

        classgameran = GameRandom()
        classgameran.main_random()

    elif version_selected.lower() == 'd':
        classdeck.generate_decks(number_decks)

        classgamedif = GameDif()
        classgamedif.play_dif()

    else:
        quit()

main()