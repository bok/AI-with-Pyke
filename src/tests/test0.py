# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################



from agent import UAgent
from object import UObject
from universe import Universe
from test import Test

class Test(Test):

    def __init__(self):
        """ Trivial test
        Alice is at location 0, can move, and wants herself to be in location 1.
        Expected result : Alice moves from 0 to 1."""
        alice = UAgent( 'Alice',
                        ['move'],
                        [('know', 'Alice', ('location', 'Alice', 1))]
                )

        uni = Universe(2)
        uni.add(alice, 0)

        self.agents = [alice]
        self.objects = []
        self.universe = uni
        self.nb_iteration_max = 2
        self.test_name = 'Test of the move action.'
