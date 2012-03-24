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
        if hand.total() < 17:
            return True
        else:
            return False

    def add(self, hands):
        self.hands.extend(hands)

    def increase(self, amount):
        self.chips = self.chips + amount

    def decrease(self, amount):
        self.chips = self.chips - amount
