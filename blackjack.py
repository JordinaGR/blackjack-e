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

        random.shuffle(self.deck)
        return self.deck

    def gen_two_cards(self):
        c1 = self.deck.pop()
        c2 = self.deck.pop()
        pc1 = self.deck.pop()
        pc2 = self.deck.pop()

        return c1, c2, pc1, pc2

    def get_one_card(self):
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
        classgagmedeal = GameDeal()

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

        self.player_play(result_player, result_comp, True, True, pc1, pc2, bet, c1, c2, wclass, money)

    def player_play(self, result_player, result_comp, possible, possiblec, pc1, pc2, bet, c1, c2, wclass, money):
        have_Aplayer = 0
        if c1 == 'A':
            have_Aplayer += 1
        if c2 == 'A':
            have_Aplayer += 1

        while possible is True:
            if result_player > 21 and have_Aplayer == 0:
                print(f'You lost! {result_comp} to {result_player}')
                money -= bet
                self.start_play('r', money)
            
            elif result_player > 21 and have_Aplayer > 0:
                result_player -= 10
                have_Aplayer -= 1

            elif result_player == 21:
                print('Blackjack, you win')
                money = (money + bet) + (bet/2)
                self.start_play('r', money)

            morecard = str(input("\nHit or stand? (h/s) "))

            if morecard.lower() == 'h':
                tmp = self.get_one_card()
                if tmp  == 'A':
                    have_Aplayer += 1
                result_player = self.add_cards(result_player, tmp)
                print(tmp)
                time.sleep(2)

            elif morecard.lower() == 's':
                print('You got a ', result_player)
                time.sleep(2)
                possible = False

        print(f"\nComputer had {pc1} and {pc2}")
        time.sleep(2)

        if wclass == 'r':
            classgamerandom = GameRandom()
            result_comp = classgamerandom.comp_random_play(result_player, result_comp, possible, possiblec, pc1, pc2, bet, c1, c2, money)
        
        elif wclass == 'd':
            classgamedif = GameDif()
            result_comp = classgamedif.round_dif(result_player, result_comp, possible, possiblec, pc1, pc2, bet, c1, c2, money)

        if result_comp == result_player:
            print(f"\nIt was a draw {result_comp} to {result_player}")
            money -= bet

        if result_comp > result_player:
            print(f"\nThe computer won {result_comp} to {result_player} ")
            money -= bet

        if result_comp < result_player:
            print(f"\nYou won {result_player} to {result_comp} ")
            money += bet

        self.start_play('r', money)

class GameRandom(Deck):

    money = 5000

    def comp_random_play(self, result_player, result_comp, possible, possiblec, pc1, pc2, bet, c1, c2, money):
        
        have_Acomp = 0
        if c1 == 'A':
            have_Acomp += 1
        if c2 == 'A':
            have_Acomp += 1

        while possiblec is True:

            if result_comp > 21 and have_Acomp > 0:
                result_comp -= 10
                have_Acomp -= 1

            if result_comp > 21 and have_Acomp == 0:
                print(f'You win! {result_comp} to {result_player}')
                money += bet
                super().start_play('r', money)
            elif result_comp == 21:
                print('Blackjack, comp win')
                money = (money - bet) - (bet/2)
                super().start_play('r', money)

            if result_comp < 17:
                tmp = super().get_one_card()
                if tmp  == 'A':
                    have_Acomp += 1
                print(f"\nComputer took {tmp}")
                time.sleep(2)
                result_comp = super().add_cards(result_comp, tmp)

            elif result_comp >= 17:
                print('\nThe computer does not take a card')
                time.sleep(2)
                possiblec = False

        return result_comp

    def main_random(self):
        super().start_play('r', self.money)

class GameDif(Deck):

    money = 1000

    def comp_takes(self, result_player, result_comp):
        if result_player == result_comp:
            return False
        if result_player > result_comp:
            return True
        if result_player < result_comp:
            return False

    def round_dif(self, result_player, result_comp, possible, possiblec, pc1, pc2, bet, c1, c2, money):

        have_Acomp = 0
        if c1 == 'A':
            have_Acomp += 1
        if c2 == 'A':
            have_Acomp += 1

        while possiblec is True:

            if result_comp > 21 and have_Acomp > 0:
                result_comp -= 10
                have_Acomp -= 1

            if result_comp > 21 and have_Acomp == 0:
                print(f'You win! {result_comp} to {result_player}')
                money += bet
                super().start_play('r', money)
            elif result_comp == 21:
                print('Blackjack, comp win')
                money = (money - bet) - (bet/2)
                super().start_play('r', money)
            
            hitstand = self.comp_takes(result_player, result_comp)

            if hitstand is True:
                tmp = super().get_one_card()
                if tmp  == 'A':
                    have_Acomp += 1
                print(f"\nComputer took {tmp}")
                time.sleep(2)
                result_comp = super().add_cards(result_comp, tmp)

            elif hitstand is False:
                print('\nThe computer does not take a card')
                time.sleep(2)
                possiblec = False

        return result_comp

    def play_dif(self):
        super().start_play('d', self.money)


class GameDeal(Deck):

    money = 1000
    money1 = 1000
    base = 20
    count = 0
    true_count = 0
    bet = 20

    def count_cards(self, card):
        if type(card) == str or card == 10:
            self.count -= 1
        elif card >= 2 and card <= 6:
            self.count += 1
        
        return self.count

    def gen_two_cards(self):
        c1 = super().deck.pop()
        c2 = super().deck.pop()
        pc1 = super().deck.pop()
        pc2 = super().deck.pop()

        self.count_cards(c1)
        self.count_cards(c2)
        self.count_cards(pc1)
        self.count_cards(pc2)

        return c1, c2, pc1, pc2

    def get_one_card(self):
        ec = self.deck.pop()

        self.count_cards(ec)

        return ec

    def hardtotals(self, result_comp, c1):
        if type(c1) == str:
            c1 = super().letter_cards_values[c1]
        if result_comp >= 17 or (result_comp == 12 and (c1 >= 4 and c1 <= 6)):
            return False
        if (result_comp >= 13 and result_comp <= 16) and (c1 >= 7 and c1 <= 11):
            return True
        if result_comp == 12 and (c1 == 2 or c1 == 3 or (c1 >=7 and c1 <= 11)) or (result_comp <= 8):
            return True
        if (result_comp >= 13 and result_comp <= 16) and (c1 >= 2 and c1 <= 6):
            return False
        if (result_comp == 11) or (result_comp == 10 and (c1 >= 2 and c1 <= 9)) or (result_comp == 9 and (c1 >= 3 and c1 <= 6)):
            self.bet *= 2
            print("Computer dobles the bet and hit")
            return True
        if (result_comp == 9 and (c1 == 2 or (c1 >= 7 and c1 <= 11))) or (result_comp == 10 and (c1 >= 10 and c1 <= 11)):
            return False

    def softtotals(self, c1, num):
        if type(c1) == str:
            c1 = super().letter_cards_values[c1]

        if num == 8 and c1 == 6:
            print("Computer dobles de bet and stands")
            self.bet *= 2
            return False
        if num == 9 or num == 8:
            return False
        if (num == 7) and (c1 >= 7 and c1 <= 8):
            return False
        if num == 7 and (c1 >= 2 and c1 >= 6):
            print("Computer dobles de bet and stands")
            self.bet *= 2
            return False
        elif (num == 7) and (c1 == 9 or c1 == 10 or c1 == 11):
            return True
        if (num >= 2 and num <= 6):
            if (c1 == 5 or c1 == 6) or ((num >= 4 and num <= 6) and c1 == 4) or (num == 6 and c1 == 3):
                print("Computer dobles the bet and hit")
                self.bet *= 2
                return True
            else:
                return True

    def hitstand(self, c1, result_comp, recursion, ace, num):
        if recursion == 0:
            if ace is None:
                return self.hardtotals(result_comp, c1)
            if ace is not None:
                return self.softtotals(c1, num)

        if recursion > 0:
            return self.hardtotals(result_comp, c1)

    def bet_amount(self):
        self.true_count = self.count / (len(super().deck) / 52)

        if self.true_count < 2:
            self.bet = self.base
        elif self.true_count >= 2 and self.true_count < 4:
            self.bet = self.base * 2
        elif self.true_count >= 4 and self.true_count < 6:
            self.bet = self.base * 3
        elif self.true_count >= 6 and self.true_count < 8:
            self.bet = self.base * 4
        elif self.true_count >= 8:
            self.bet = self.base * 5

        return self.bet

    def round(self,result_player, result_comp, possible, possiblec, pc1, pc2, c1, c2, number_decks, ace, num ):
        have_Acomp = 0
        if pc1 == 'A':
            have_Acomp += 1
            ace = pc1
            num = pc2

        if pc2 == 'A':
            have_Acomp += 1
            ace = pc2
            num = pc1
        
        if pc2 == 'A' and pc1 == 'A':
            num = pc1
            num = pc2

        recursion = 0

        while possiblec is True:

            if result_comp > 21 and have_Acomp > 0:
                result_comp -= 10
                have_Acomp -= 1

            if result_comp > 21 and have_Acomp == 0:
                print(f'You win! {result_comp} to {result_player}')
                self.money -= self.bet
                self.main(number_decks)

            elif result_comp == 21:
                print('Blackjack, comp win')
                self.money += (self.bet + (self.bet/2))
                self.main(number_decks)

            hitstandd = self.hitstand(c1, result_comp, recursion, ace, num)
            recursion += 1

            if hitstandd is True:
                tmp = self.get_one_card()
                if tmp == 'A':
                    have_Acomp += 1
                    ace = tmp
                print(f"\nComputer took {tmp}")
                time.sleep(2)
                result_comp = super().add_cards(result_comp, tmp)

            elif hitstandd is False:
                print('\nThe computer does not take a card')
                time.sleep(2)
                possiblec = False

        have_Aplayer = 0
        if c1 == 'A':
            have_Aplayer += 1
        if c2 == 'A':
            have_Aplayer += 1

        print(f"\nYour cards are {c1} and {c2}")

        while possible is True:
            if result_player > 21 and have_Aplayer == 0:
                print(f'You lost! {result_comp} to {result_player}')
                self.money += self.bet
                self.main(number_decks)
            
            elif result_player > 21 and have_Aplayer > 0:
                result_player -= 10
                have_Aplayer -= 1

            elif result_player == 21:
                print('Blackjack, you win')
                self.money += (self.bet + (self.bet/2))
                self.main(number_decks)

            morecard = str(input("\nHit or stand? (h/s) "))

            if morecard.lower() == 'h':
                tmp = self.get_one_card()
                if tmp  == 'A':
                    have_Aplayer += 1
                result_player = super().add_cards(result_player, tmp)
                print(tmp)
                time.sleep(2)

            elif morecard.lower() == 's':
                print('You got a ', result_player)
                time.sleep(2)
                possible = False

        if result_comp == result_player:
            print(f"\nIt was a draw {result_comp} to {result_player}")
            self.money -= self.bet

        if result_comp > result_player:
            print(f"\nThe computer won {result_comp} to {result_player} ")
            self.money += self.bet

        if result_comp < result_player:
            print(f"\nYou won {result_player} to {result_comp} ")
            self.money -= self.bet

        self.main(number_decks)

    def main(self, number_decks):

        if len(super().deck) <= 10:
            print(f"\nThe computer gained {self.money - self.money1} this round.")
            print("\nNot enought cards, the match is over\n")
            main()

        time.sleep(3)
        print('________________________________________________________________________________')

        if self.money == 0:
            print("Computer doesn't have enough money\n")
            main()

        c1, c2, pc1, pc2 = self.gen_two_cards()

        bet = self.bet_amount()
        if bet > self.money:
            bet = bet / 2
            self.main(number_decks)
        
        self.bet = bet
        print(f"The computer bet is {self.bet} and has {self.money} left")

        print(f"\nYour cards are: {c1} and {'X'} ")

        print(f"Computer cards are: {pc1} and {pc2}")

        result_player = super().add_cards(c1, c2)
        result_comp = super().add_cards(pc1, pc2)

        self.round(result_player, result_comp, True, True, pc1, pc2, c1, c2, number_decks, None, None)

def main():
    print("LET'S PLAY BLACKJACK")
    version_selected = str(input('Do you wanna play the random version (r), the dificult (d) or to be the dealer (de) '))
    number_decks = int(input('How many decks do you wanna play with? ' ))
    classdeck = Deck()
    classdeck.generate_decks(number_decks)

    if version_selected.lower() == 'r':
        classgameran = GameRandom()
        classgameran.main_random()

    elif version_selected.lower() == 'd':
        classgamedif = GameDif()
        classgamedif.play_dif()

    else:
        classgamedeal = GameDeal()
        classgamedeal.main(number_decks)

main()