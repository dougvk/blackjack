#!/usr/bin/python
import unittest
from hand import *
from table import *
from card import *

class Player():

    # create a player associated with a table, a set of hands, and chips to bet with
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
            if self.chips >= hand.bet * 2:
                hand.ante(hand.bet * 2)
                return True
            return False
        return False

    def add(self, hands):
        self.hands.extend(hands)

    def increase(self, amount):
        self.chips = self.chips + amount

    def decrease(self, amount):
        self.chips = self.chips - amount

class TestHand(unittest.TestCase):
    def setUp(self):
        self.t = Table(10)
        self.p = Player(self.t)
        self.upcard = BlackjackCard(BlackjackCard.ten)
        self.eightcard = BlackjackCard(BlackjackCard.eight)
        self.acecard = BlackjackCard(BlackjackCard.ace)
        self.downcard = BlackjackCard(BlackjackCard.two)

    def testChips(self):
        self.assertEqual(500,self.p.chips)
        self.p.increase(10)
        self.assertEqual(510,self.p.chips)
        self.p.decrease(10)
        self.assertEqual(500,self.p.chips)

    def testBet(self):
        self.p.place_bet()
        self.assertEqual(1,len(self.p.hands))
        hand = self.p.get_first_hand()
        self.assertEqual(10,hand.bet)

        hand.add(self.upcard)
        hand.add(self.downcard)
        self.t.upcard = self.downcard
        self.assertEqual(False, self.p.hit(hand))

        self.t.upcard = self.upcard
        self.assertEqual(True, self.p.hit(hand))
        hand.add(self.downcard)
        self.assertEqual(True, self.p.hit(hand))
        hand.add(self.downcard)
        self.assertEqual(True, self.p.hit(hand))
        hand.add(self.downcard)
        self.assertEqual(False, self.p.hit(hand))

    def test_advanced(self):
        self.p.place_bet()
        hand = self.p.get_first_hand()
        hand.add(self.upcard)
        hand.add(self.downcard)
        self.assertEqual(False, self.p.double_down(hand))
        self.assertEqual(False, self.p.split(hand))
        hand.hand[0] = self.eightcard
        self.p.chips = 10
        self.assertEqual(False, self.p.double_down(hand))
        self.assertEqual(10, hand.bet)
        self.p.chips = 100
        self.assertEqual(True, self.p.double_down(hand))
        self.assertEqual(20, hand.bet)

        hand.hand[1] = self.upcard
        hand.hand[0] = self.upcard
        self.assertEqual(True, self.p.split(hand))
        self.assertEqual(2, len(self.p.hands))
        self.assertEqual(1, len(self.p.hands[0].hand))
        self.assertEqual(1, len(self.p.hands[1].hand))

if __name__ == "__main__":
    unittest.main()
