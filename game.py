#!/usr/bin/python
import unittest
from player import *

class Game():
    def __init__(self, shoe, table):
        self.shoe = shoe.cards
        self.table = table
        self.dealer = Player(self.table)

    def execute_round(self):
        for player in self.table.players:
            player.place_bet()
            hand = player.get_first_hand()
            hand.add(self.shoe.pop())
            hand.add(self.shoe.pop())

        self.dealer.hands = [Hand()]
        dealer_hand = self.dealer.get_first_hand()
        dealer_hand.add(self.shoe.pop())
        dealer_hand.add(self.shoe.pop())

        for index,player in enumerate(self.table.players):
            for hand in player.hands:
                print "-------------"
                while player.hit(hand):
                    print "Player %s hitting hand %s" % (index, hand)
                    hand.add(self.shoe.pop())
                print "Player %s standing hand %s" % (index, hand)

        while dealer_hand.total() < 17:
            print "Dealer hitting hand %s" % dealer_hand
            dealer_hand.add(self.shoe.pop())
        print "Dealer standing with hand %s" % dealer_hand

        print str(self.table)
