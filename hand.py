#!/usr/bin/python
import unittest
from card import *

class Hand():
    
    def __init__(self, first, second, dealer):
        self.hand = [first, second]
        self.dealer = dealer

    def add(self, card):
        self.hand.append(card)
    
    def hard_total(self):
        return sum(map(lambda x: x.rank, self.hand))

    def soft_total(self):
        hard_total = map(lambda x: x.rank, self.hand)
        if 1 in hard_total:
            soft_total = sum(hard_total) + 10
            return soft_total if soft_total <= 21 else hard_total
    
    def upcard(self)
        return self.hand[0].rank

class TestHand(unittest.TestCase):
    def setUp(self):
        self.upcard = BlackjackCard(BlackjackCard.ten)
        self.downcard = BlackjackCard(BlackjackCard.two)
        self.acecard = BlackjackCard(BlackjackCard.ace)

        self.hand_player = Hand(self.upcard, self.downcard, False)
        self.hand_dealer = Hand(self.upcard, self.downcard, True)

        self.ace_player = Hand(self.acecard, self.downcard, False)
        self.ace_dealer = Hand(self.acecard, self.downcard, True)

        self.two_ace_player = Hand(self.acecard, self.downcard, False)
        self.two_ace_dealer = Hand(self.acecard, self.downcard, True)
        self.two_ace_player.add(self.acecard)
        self.two_ace_dealer.add(self.acecard)

        self.three_ace_player = Hand(self.acecard, self.downcard, False)
        self.three_ace_dealer = Hand(self.acecard, self.downcard, True)
        self.three_ace_player.add(self.acecard)
        self.three_ace_dealer.add(self.acecard)
        self.three_ace_player.add(self.acecard)
        self.three_ace_dealer.add(self.acecard)

        self.bust_player = Hand(self.upcard, self.downcard, False)
        self.bust_dealer = Hand(self.upcard, self.downcard, True)
        self.bust_player.add(self.upcard)
        self.bust_dealer.add(self.upcard)

        self.bust_ace_player = Hand(self.upcard, self.downcard, False)
        self.bust_ace_dealer = Hand(self.upcard, self.downcard, True)
        self.bust_ace_player.add(self.upcard)
        self.bust_ace_dealer.add(self.upcard)
        self.bust_ace_player.add(self.acecard)
        self.bust_ace_dealer.add(self.acecard)

    def test_hard_value(self):
        self.assertEqual(self.hand_player.hard_total(), 12)
        self.assertEqual(self.hand_dealer.hard_total(), 12)

        self.assertEqual(self.ace_player.hard_total(), 3)
        self.assertEqual(self.ace_dealer.hard_total(), 3)

        self.assertEqual(self.two_ace_player.hard_total(), 4)
        self.assertEqual(self.two_ace_dealer.hard_total(), 4)

        self.assertEqual(self.three_ace_player.hard_total(), 5)
        self.assertEqual(self.three_ace_dealer.hard_total(), 5)

        self.assertEqual(self.bust_player.hard_total(), 22)
        self.assertEqual(self.bust_dealer.hard_total(), 22)

        self.assertEqual(self.bust_ace_player.hard_total(), 23)
        self.assertEqual(self.bust_ace_dealer.hard_total(), 23)

    def test_soft_value(self):
        self.assertEqual(self.hand_player.hard_total(), 12)
        self.assertEqual(self.hand_dealer.hard_total(), 12)

        self.assertEqual(self.ace_player.soft_total(), 13)
        self.assertEqual(self.ace_dealer.soft_total(), 13)

        self.assertEqual(self.two_ace_player.soft_total(), 14)
        self.assertEqual(self.two_ace_dealer.soft_total(), 14)

        self.assertEqual(self.three_ace_player.soft_total(), 15)
        self.assertEqual(self.three_ace_dealer.soft_total(), 15)

        self.assertEqual(self.bust_player.hard_total(), 22)
        self.assertEqual(self.bust_dealer.hard_total(), 22)

        self.assertEqual(self.bust_ace_player.hard_total(), 23)
        self.assertEqual(self.bust_ace_dealer.hard_total(), 23)

if __name__ == "__main__":
    unittest.main()
