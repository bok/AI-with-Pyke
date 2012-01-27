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
        """A basic test where Alice can move, take and put and wants to change
        the location of an object.
        Expected result : Alice moves to the item, takes it and moves it."""

        alice = UAgent( 'Alice',
                        ['move', 'take', 'put'],
                        [('know', 'Alice', ('location', 'pipo', 0)),],
                        [('know', 'Alice', ('location', 'pipo', 1)),],
                )
        pipo = UObject('pipo')

        uni = Universe(2)
        uni.add(alice, 0)
        uni.add(pipo, 1)

        self.agents = [alice]
        self.objects = [pipo]
        self.universe = uni
        self.nb_iteration_max = 4
        self.test_name = 'Test with Alice changing an object\'s position.'

