#!/usr/bin/python
import unittest
from hand import *

class Player():

    def __init__(self, table):
        self.table = table
        self.hands = []
        self.chips = 500

    def __str__(self):
        lines = ["Hands for this player: "]
        for hand in self.hands:
            lines.append("%s" % hand)
        return '\n'.join(lines)

    def place_bet(self):
        self.hands = [Hand()]
        self.hands[0].ante(self.table.minimum_bet)

    def get_first_hand(self):
        return self.hands[0]

    def hit(self,hand):
        if hand.total() < 17 and hand.total() < self.table.upcard.rank + 10:
            return True
        else:
            return False

    def split(self,hand):
        if hand.hand[0].rank == hand.hand[1].rank:
            new_hand = Hand()
            new_hand.add(hand.hand.pop())
            new_hand.ante(self.table.minimum_bet)
            self.add([new_hand])
            return True
        return False

    def double_down(self, hand):
        if hand.total() == 10 or hand.total() == 11:
            hand.ante(hand.bet * 2)
            return True
        return False

    def add(self, hands):
        self.hands.extend(hands)

    def increase(self, amount):
        self.chips = self.chips + amount

    def decrease(self, amount):
        self.chips = self.chips - amount
