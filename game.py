#!/usr/bin/python
import unittest
from player import *

class Game():
    def __init__(self, shoe, table):
        self.shoe = shoe
        self.table = table
        self.dealer = Player(self.table)

    def execute_round(self):
        active_players = [player for player in self.table.players if player.chips >= self.table.minimum_bet]
        if len(active_players) == 0:
            return False
        for player in active_players:
            player.place_bet()
            hand = player.get_first_hand()
            hand.add(self.shoe.popcard())
            hand.add(self.shoe.popcard())

        self.dealer.hands = [Hand()]
        dealer_hand = self.dealer.get_first_hand()
        dealer_hand.add(self.shoe.popcard())
        dealer_hand.add(self.shoe.popcard())

        for index,player in enumerate(active_players):
            for hand in player.hands:
                print "-------------"
                while player.hit(hand):
                    print "Player %s hitting %s" % (index, hand)
                    hand.add(self.shoe.popcard())
                print "Player %s standing %s" % (index, hand)

        print "-------------"
        while dealer_hand.total() < 17:
            print "Dealer hitting %s" % dealer_hand
            dealer_hand.add(self.shoe.popcard())
        print "Dealer standing with %s" % dealer_hand

        dealer_total = dealer_hand.total()
        for index,player in enumerate(active_players):
            for hand in player.hands:
                print "-------------"
                hand_total = hand.total()
                if hand_total > 21:
                    print "Player %s busts on %s" % (index, hand)
                    player.decrease(hand.bet)
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
