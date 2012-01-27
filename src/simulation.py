#!/usr/bin/python2
# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################

# A single simulation to run.

from agent import UAgent
from object import UObject
from universe import Universe

alice = UAgent( name='Alice',
                can_do=['take', 'ask_if', 'ask_ref'],
                goals=
                [
                    (('know', 'Alice', ('location', 'pipo', 'Alice')),),
                ],
                knowledge=[],
                max_length_plan = 3
        )

bob = UAgent( name='Bob',
              can_do=['move', 'inform_if', 'inform_ref'],
              goals=[],
              knowledge=
              [
                ('know', 'Bob', ('location', 'pipo', 0))
              ]
      )

pipo = UObject('pipo')

uni = Universe(3)
uni.add(alice, 0)
uni.add(bob, 2)
uni.add(pipo, 0)

print(uni)

finished = False
i = 0
nb_iteration_max = 5

while not finished and i < nb_iteration_max:
    print 'Itération %d' % i
    uni.step()
    i += 1
    finished = uni.all_satisfied

if i == nb_iteration_max:
    print 'Maximum number of iterations reached.'
