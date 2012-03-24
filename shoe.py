#!/usr/bin/python
import unittest
import random
from card import *

class Shoe():
    num_decks = 5

    def __init__(self, cards):
        if cards is not None:
            self.cards = cards
            self.plastic_card = int(.8 * len(cards))
            self.shuffle()

    # decided to implement my own shuffle for the hell of it
    # O(n) with n calls to random number generator
    def shuffle(self):
        for i in range(len(self.cards),0,-1):
            swap_index = int(random.random() * (i-1))
            self.cards[swap_index], self.cards[i-1] = self.cards[i-1], self.cards[swap_index]

    def deal_full(self):
        for card in self.cards:
            yield card

    def deal_plastic(self):
        for index, card in enumerate(self.cards):
            if index < self.plastic_card:
                yield card

    def popcard(self):
        if len(self.cards) == 0:
            self.create_blackjack_shoe()
            return self.cards.pop()
        else:
            return self.cards.pop()

    def create_blackjack_shoe(self):
        cards = [BlackjackCard(BlackjackCard.ace) , BlackjackCard(BlackjackCard.two) , \
            BlackjackCard(BlackjackCard.three) , BlackjackCard(BlackjackCard.four) , \
            BlackjackCard(BlackjackCard.five) , BlackjackCard(BlackjackCard.six) , \
            BlackjackCard(BlackjackCard.seven) , BlackjackCard(BlackjackCard.eight) , \
            BlackjackCard(BlackjackCard.nine) , BlackjackCard(BlackjackCard.ten) , \
            BlackjackCard(BlackjackCard.jack) , BlackjackCard(BlackjackCard.queen) , \
            BlackjackCard(BlackjackCard.king)]
        self.cards = cards * 4 * Shoe.num_decks
        self.plastic_card = int(.8 * len(self.cards))
        self.shuffle()

class TestShoe(unittest.TestCase):
    def setUp(self):
        self.cards = [BlackjackCard(BlackjackCard.ace) , BlackjackCard(BlackjackCard.two) , \
            BlackjackCard(BlackjackCard.three) , BlackjackCard(BlackjackCard.four) , \
            BlackjackCard(BlackjackCard.five) , BlackjackCard(BlackjackCard.six) , \
            BlackjackCard(BlackjackCard.seven) , BlackjackCard(BlackjackCard.eight) , \
            BlackjackCard(BlackjackCard.nine) , BlackjackCard(BlackjackCard.ten) , \
            BlackjackCard(BlackjackCard.jack) , BlackjackCard(BlackjackCard.queen) , \
            BlackjackCard(BlackjackCard.king)]
        self.deck = Shoe(self.cards * 4)
        self.shoe = Shoe(self.cards * 4 * Shoe.num_decks)

    def test_shuffle(self):
        self.deck.shuffle()
        self.shoe.shuffle()

        rank_shuffled_deck = map(lambda x: x.rank, self.deck.cards)
        rank_shuffled_shoe = map(lambda x: x.rank, self.shoe.cards)

        softrank_shuffled_deck = map(lambda x: x.soft_rank(), self.deck.cards)
        softrank_shuffled_shoe = map(lambda x: x.soft_rank(), self.shoe.cards)

        hard_deck_value = (sum(range(1,11)) + 10*3) * 4
        hard_shoe_value = hard_deck_value * Shoe.num_decks

        soft_deck_value = (sum(range(2,11)) + 10*3 + 11) * 4
        soft_shoe_value = soft_deck_value * Shoe.num_decks

        self.assertEqual(sum(rank_shuffled_deck), hard_deck_value)
        self.assertEqual(sum(rank_shuffled_shoe), hard_shoe_value)

        self.assertEqual(sum(softrank_shuffled_deck), soft_deck_value)
        self.assertEqual(sum(softrank_shuffled_shoe), soft_shoe_value)

    def test_shoe(self):
        self.assertEqual(52, len(self.deck.cards))
        self.assertEqual(52*Shoe.num_decks, len(self.shoe.cards))
    
    def test_deal_full(self):
        hard_deck_value = (sum(range(1,11)) + 10*3) * 4
        num_cards = 0
        deck_value = 0
        for i in self.deck.deal_full():
            num_cards = num_cards + 1
            deck_value = deck_value + i.rank
        self.assertEqual(num_cards,len(self.deck.cards))
        self.assertEqual(deck_value,hard_deck_value)

        hard_shoe_value = hard_deck_value * Shoe.num_decks
        num_cards = 0
        shoe_value = 0
        for i in self.shoe.deal_full():
            num_cards = num_cards + 1
            shoe_value = shoe_value + i.rank
        self.assertEqual(num_cards, len(self.shoe.cards))
        self.assertEqual(shoe_value,hard_shoe_value)

    def test_deal_plastic(self):
        num_cards = 0
        for i in self.shoe.deal_plastic():
            num_cards = num_cards + 1
        self.assertEqual(num_cards, self.shoe.plastic_card)

if __name__ == '__main__':
    unittest.main()
