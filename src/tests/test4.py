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
        """A basic test where Alice can only order and wants to move the item.
        Bob can move and take/put items.
        Expected result : Alice orders Bob to move, take the item, move, put
        the item."""
        alice = UAgent( 'Alice',
                        can_do    = ['order'],
                        goals     = [('know', 'Alice', ('location', 'pipo',0))],
                        knowledge = [
                            ('know', 'Alice', ('location', 'pipo',2)),
                            ('know', 'Alice', ('location', 'Bob', 1)),
                            ('know', 'Alice', ('free', 'Bob', True)),
                        ]
                )
        bob = UAgent( 'Bob',
                      ['move', 'take', 'put'],
                      goals = [],
                      knowledge = [('know', 'Bob', ('location', 'pipo',2))]
                )
                      
        pipo = UObject('pipo')

        uni = Universe(3)
        uni.add(alice, 0)
        uni.add(bob, 1)
        uni.add(pipo, 2)

        self.agents = [alice, bob]
        self.objects = [pipo]
        self.universe = uni
        self.nb_iteration_max = 6
        self.test_name = 'Test with Alice ordering Bob to move the object.'
