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
        """A basic test where Alice asks Bob about the object she wants to take."""
        alice = UAgent( 'Alice',
                        ['take', 'ask_if', 'ask_ref'],
                        [
                            (('know', 'Alice', ('location', 'pipo', 'Alice')),),
                        ],
                        [],
                        max_length_plan = 3
                )

        bob = UAgent( 'Bob',
                      ['move', 'inform_if', 'inform_ref'],
                      [],
                      [
                        ('know', 'Bob', ('location', 'pipo', 0))
                      ]      
              )
                      
        pipo = UObject('pipo')

        uni = Universe(3)
        uni.add(alice, 0)
        uni.add(bob, 2)
        uni.add(pipo, 0)

        self.agents = [alice, bob]
        self.objects = [pipo]
        self.universe = uni
        self.nb_iteration_max = 6
        self.test_name = 'Test with Alice asking Bob about the object.'


