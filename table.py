#!/usr/bin/python
import unittest

class Table():

    def __init__(self, minimum_bet):
        self.players = []
        self.minimum_bet = minimum_bet

    def __str__(self):
        lines = ["---------\nThis is the table:"]
        for index, player in enumerate(self.players):
            lines.append("---------\nThis is player %s with %s chips:\n%s" % (index, player.chips, player))
        return '\n'.join(lines)

    def add(self, players):
        self.players.extend(players)
