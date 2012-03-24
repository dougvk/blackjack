#!/usr/bin/python
import unittest
from card import *

class Hand():
    
    def __init__(self, first, second, dealer):
        self.hand = [first, second]
        self.dealer = dealer

    def __str__(self):
        return "The Hand: %s" % self.hand

    def add(self, card):
        self.hand.append(card)
    
    def hard_total(self):
        return sum(map(lambda x: x.rank, self.hand))

    def total(self):
        hard_hand = map(lambda x: x.rank, self.hand)
        if 1 in hard_hand:
            soft_total = sum(hard_hand) + 10
            return soft_total if soft_total <= 21 else sum(hard_hand)
        return sum(hard_hand)
    
    def upcard(self):
        return self.hand[0].rank

    def blackjack(self):
        return len(self.hand) == 2 and self.total() == 21

    def bust(self):
        return self.total() > 21

class TestHand(unittest.TestCase):
    def setUp(self):
        self.upcard = BlackjackCard(BlackjackCard.ten)
        self.downcard = BlackjackCard(BlackjackCard.two)
        self.acecard = BlackjackCard(BlackjackCard.ace)

        self.hand_player = Hand(self.upcard, self.downcard, False)

        self.ace_player = Hand(self.acecard, self.downcard, False)

        self.two_ace_player = Hand(self.acecard, self.downcard, False)
        self.two_ace_player.add(self.acecard)

        self.three_ace_player = Hand(self.acecard, self.downcard, False)
        self.three_ace_player.add(self.acecard)
        self.three_ace_player.add(self.acecard)

        self.bust_player = Hand(self.upcard, self.downcard, False)
        self.bust_player.add(self.upcard)

        self.bust_ace_player = Hand(self.upcard, self.downcard, False)
        self.bust_ace_player.add(self.upcard)
        self.bust_ace_player.add(self.acecard)

        self.blackjack_player = Hand(self.upcard, self.acecard, False)

    def test_hard_value(self):
        self.assertEqual(self.hand_player.hard_total(), 12)
        self.assertEqual(self.ace_player.hard_total(), 3)
        self.assertEqual(self.two_ace_player.hard_total(), 4)
        self.assertEqual(self.three_ace_player.hard_total(), 5)
        self.assertEqual(self.bust_player.hard_total(), 22)
        self.assertEqual(self.bust_ace_player.hard_total(), 23)

    def test_soft_value(self):
        self.assertEqual(self.hand_player.total(), 12)
        self.assertEqual(self.ace_player.total(), 13)
        self.assertEqual(self.two_ace_player.total(), 14)
        self.assertEqual(self.three_ace_player.total(), 15)
        self.assertEqual(self.bust_player.total(), 22)
        self.assertEqual(self.bust_ace_player.total(), 23)

    def test_busted(self):
        self.assertEqual(True, self.bust_player.bust())
        self.assertEqual(True, self.bust_ace_player.bust())
        self.assertEqual(False, self.hand_player.bust())
        self.assertEqual(False, self.ace_player.bust())
        self.assertEqual(False, self.two_ace_player.bust())
        self.assertEqual(False, self.three_ace_player.bust())

    def test_blackjack(self):
        self.assertEqual(False, self.bust_player.blackjack())
        self.assertEqual(False, self.bust_ace_player.blackjack())
        self.assertEqual(False, self.hand_player.blackjack())
        self.assertEqual(False, self.ace_player.blackjack())
        self.assertEqual(False, self.two_ace_player.blackjack())
        self.assertEqual(False, self.three_ace_player.blackjack())
        self.assertEqual(True, self.blackjack_player.blackjack())

if __name__ == "__main__":
    unittest.main()
