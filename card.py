#!/usr/bin/python
import unittest

class BlackjackCard():
    jack, queen, king = 10, 10, 10
    ace = 1
    two, three, four, five, six, seven, eight, nine, ten = 2, 3, 4, 5, 6, 7, 8, 9, 10

    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return "Card(%s)" % self.rank

    def soft_rank(self):
        if self.rank == 1:
            return 11
        else:
            return self.rank

class TestBlackjackCard(unittest.TestCase):
    def setUp(self):
        self.card_ranks = [BlackjackCard.ace , BlackjackCard.two , BlackjackCard.three , \
            BlackjackCard.four , BlackjackCard.five , BlackjackCard.six , \
            BlackjackCard.seven , BlackjackCard.eight , BlackjackCard.nine , \
            BlackjackCard.ten , BlackjackCard.jack , BlackjackCard.queen, \
            BlackjackCard.king]
        self.cards_to_test = [BlackjackCard(BlackjackCard.ace) , BlackjackCard(BlackjackCard.two) , \
                BlackjackCard(BlackjackCard.three) , BlackjackCard(BlackjackCard.four) , \
                BlackjackCard(BlackjackCard.five) , BlackjackCard(BlackjackCard.six) , \
                BlackjackCard(BlackjackCard.seven) , BlackjackCard(BlackjackCard.eight) , \
                BlackjackCard(BlackjackCard.nine) , BlackjackCard(BlackjackCard.ten) , \
                BlackjackCard(BlackjackCard.jack) , BlackjackCard(BlackjackCard.queen) , \
                BlackjackCard(BlackjackCard.king)]

    def test_rank(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9,10,10,10,10], self.card_ranks)
        rank_list = map(lambda x: x.rank, self.cards_to_test)
        soft_rank_list = map(lambda x: x.soft_rank(), self.cards_to_test)
        self.assertEqual([1,2,3,4,5,6,7,8,9,10,10,10,10], rank_list) 
        self.assertEqual([11,2,3,4,5,6,7,8,9,10,10,10,10], soft_rank_list) 

if __name__ == '__main__':
    unittest.main()
