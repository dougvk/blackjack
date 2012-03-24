from table import *
from player import *
from shoe import *
from game import *

t = Table(10)
p = Player(t)
p2 = Player(t)
p3 = Player(t)
p4 = Player(t)
s = Shoe(None)
s.create_blackjack_shoe()
t.add([p,p2,p3,p4])

g = Game(s,t)

g.execute_round()
