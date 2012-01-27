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
        """Basic test where Alice can only order and Bob can only move. Alice
        wants Bob to change his location.
        Expected result : Alice orders Bob to move."""

        alice = UAgent( 'Alice',
                        ['order'],
                        [('know', 'Alice', ('location', 'Bob', 2))],
                        [('know', 'Alice', ('location', 'Bob', 1))]
                )
        bob = UAgent( 'Bob',
                      ['move'],
                      []
                )

        uni = Universe(3)
        uni.add(alice, 0)
        uni.add(bob, 1)

        self.agents = [alice, bob]
        self.objects = []
        self.universe = uni
        self.nb_iteration_max = 3
        self.test_name = 'Test of Alice ordering moving to Bob.'
