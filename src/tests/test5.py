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
from object_box import Box
from universe import Universe
from test import Test

class Test(Test):

    def __init__(self):
        """A basic test where Alice puts objects in a box."""
        alice = UAgent( 'Alice',
                        ['move', 'take', 'put', 'place_in_box', 'fetch_from_box'],
                        [
                            (('know', 'Alice', ('location', 'pipo', 'pipobox')),),
                            (('know', 'Alice', ('location', 'pipo2', 'pipobox')),)
                        ],
                        knowledge = [
                            ('know', 'Alice', ('location', 'pipo', 1)),
                            ('know', 'Alice', ('location', 'pipo2', 1)),
                            ('know', 'Alice', ('location', 'pipobox', 2)),
                            ('know', 'Alice', ('full', 'pipobox', False)),
                        ],
                        max_length_plan = 9
                )

        pipo = UObject('pipo')
        pipo2 = UObject('pipo2')
        pipobox = Box('pipobox', 2)

        uni = Universe(3)
        uni.add(alice, 0)
        uni.add(pipo, 1)
        uni.add(pipobox, 2)
        uni.add(pipo2, 1)

        self.agents = [alice]
        self.objects = [pipo, pipo2, pipobox]
        self.universe = uni
        self.nb_iteration_max = 9
        self.test_name = 'Test with Alice putting 2 objects in the box'

