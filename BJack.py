import random

class Deck:
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.deck = [(card, suit) for card in self.cards for suit in self.suits]
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)

class Player:
    def __init__(self):
        self.cards = []
        self.score = 0

    def hit(self, card):
        self.cards.append(card)
        self.score += self.get_card_value(card)

    def get_card_value(self, card):
        if card[0] in ['Jack', 'Queen', 'King']:
            return 10
        elif card[0] == 'Ace':
            if self.score + 11 > 21:
                return 1
            else:
                return 11
        else:
            return int(card[0])

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.player.hit(self.deck.deal_card())
        self.player.hit(self.deck.deal_card())
        self.dealer.hit(self.deck.deal_card())
        self.dealer.hit(self.deck.deal_card())

    def play_game(self):
        print("Player's cards:")
        self.show_cards(self.player.cards)
        print("Dealer's cards:")
        self.show_cards([self.dealer.cards[0], ('Hidden', 'Card')])
        if self.player.score == 21:
            print("Blackjack! Player wins!")
            return
        while self.player.score < 21:
            hit_or_stand = input("Do you want to hit or stand? ")
            if hit_or_stand.lower() == "hit":
                self.player.hit(self.deck.deal_card())
                print("Player's cards:")
                self.show_cards(self.player.cards)
                print("Dealer's cards:")
                self.show_cards([self.dealer.cards[0], ('Hidden', 'Card')])
                if self.player.score > 21:
                    print("Bust! Dealer wins!")
                    return
            else:
                break
        while self.dealer.score < 17:
            self.dealer.hit(self.deck.deal_card())
        print("Player's cards:")
        self.show_cards(self.player.cards)
        print("Dealer's cards:")
        self.show_cards(self.dealer.cards)
        if self.dealer.score > 21:
            print("Dealer bust! Player wins!")
        elif self.dealer.score > self.player.score:
            print("Dealer wins!")
        elif self.dealer.score < self.player.score:
            print("Player wins!")
        else:
            print("Push!")

    def show_cards(self, cards):
        for card in cards:
            print(card[0], "of", card[1])
            print("Score:", self.calculate_score(cards))

    def calculate_score(self, cards):
        score = 0
        for card in cards:
            score += self.player.get_card_value(card)
            return score

    def start_game(self):
        while True:
            self.play_game()
            play_again = input("Do you want to play again? (y/n)")
            if play_again.lower() == "n":
                break

game = Game()
game.start_game()




