#!/usr/bin/python
import unittest
from player import *

class Game():
    def __init__(self, shoe, table):
        self.shoe = shoe
        self.table = table
        self.dealer = Player(self.table)

    # execute one round of blackjack
    def execute_round(self):

        # list comprehension to collect all players still available to bet
        active_players = [player for player in self.table.players if player.chips >= self.table.minimum_bet]

        # deal active players in, otherwise, end game
        if len(active_players) == 0:
            return False
        for player in active_players:
            player.place_bet()
            hand = player.get_first_hand()
            hand.add(self.shoe.popcard())
            hand.add(self.shoe.popcard())

        # give dealer new hand
        self.dealer.hands = [Hand()]
        dealer_hand = self.dealer.get_first_hand()
        dealer_hand.add(self.shoe.popcard())
        dealer_hand.add(self.shoe.popcard())
        self.table.upcard = dealer_hand.upcard()

        # if dealer blackjack, terminate round early
        if dealer_hand.blackjack():
            for index,player in enumerate(active_players):
                for hand in player.hands:
                    if hand.blackjack():
                        print "Player %s pushes on dealer blackjack with %s" % (index, hand)
                    else:
                        print "Player %s loses on dealer blackjack with %s" % (index, hand)
                        player.decrease(hand.bet)
        else:
            # first check for splits and double downs
            for i,player in enumerate(active_players):
                index = 0
                print "-------------"
                while index < len(player.hands):
                    split_hand = player.hands[index]
                    if player.split(split_hand):
                        new_hand = player.hands[-1]
                        split_hand.add(self.shoe.popcard())
                        new_hand.add(self.shoe.popcard())
                        print "Player %s splitting into:\n%s\n%s" % (i, split_hand, new_hand)
                    elif player.double_down(split_hand):
                        split_hand.add(self.shoe.popcard())
                        print "Player %s doubling down %s" % (i, split_hand)
                        index = index + 1
                    else:
                        index = index + 1

            # then have all the players hit until satisfied
            for index,player in enumerate(active_players):
                for hand in player.hands:
                    print "-------------"
                    while player.hit(hand):
                        print "Player %s hitting %s" % (index, hand)
                        hand.add(self.shoe.popcard())
                    print "Player %s standing %s" % (index, hand)

            # then dealer hits until hard total >= 17
            print "-------------"
            while dealer_hand.total() < 17:
                print "Dealer hitting %s" % dealer_hand
                dealer_hand.add(self.shoe.popcard())
            print "Dealer standing with %s" % dealer_hand

            # go through and add/remove proper amounts of chips for each hand
            dealer_total = dealer_hand.total()
            for index,player in enumerate(active_players):
                for hand in player.hands:
                    print "-------------"
                    hand_total = hand.total()
                    if hand_total > 21:
                        print "Player %s busts on %s" % (index, hand)
                        player.decrease(hand.bet)
                    elif hand_total == 21 and hand.blackjack():
                        print "Player %s blackjack on %s" % (index, hand)
                        player.increase(int(hand.bet * 1.5))
                    elif dealer_total > 21 or hand_total > dealer_total:
                        print "Player %s beats dealer on %s" % (index, hand)
                        player.increase(hand.bet)
                    elif dealer_total == hand_total:
                        print "Player %s pushes dealer on %s" % (index, hand)
                    elif dealer_total > hand_total:
                        print "Player %s loses to dealer on %s" % (index, hand)
                        player.decrease(hand.bet)

        print str(self.table)
        return True
