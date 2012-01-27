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

# A generic test.
class Test:
    """The mother class of the actual tests."""
    
    def __init__(self):
        self.agents = []
        self.objects = []
        self.universe = Universe(1)
        # nb_iteration_max is here to refrain some cases to computer for
        # too long...
        self.nb_iteration_max = 1
        self.test_name = 'default_test_name'
        self.finished = False

    def run(self):
        """Run the test"""
        
        # First we print some info about the test.
        self.print_test()
        self.print_launching()
        
        # Initialization for the loop.
        self.finished = False
        i = 0

        while not self.finished and i < self.nb_iteration_max:
            print 'Iteration %d' % i
            self.universe.step()
            self.finished = self.universe.all_satisfied
            i += 1

        if i == self.nb_iteration_max:
            self.print_nbiter_atteint()

        if self.finished:
            self.print_test_successful()

        if not self.finished:
            self.print_test_failed()

        return self.finished

    def print_test(self):
        print '#####'
        print '# Test : %s' % (self.test_name)
        print '# Agents : %s' % ([agent.name for agent in self.agents])
        print '# Capacities : %s' % ([agent.can_do for agent in self.agents])
        print '# Objects : %s' % ([o.name for o in self.objects])
        print '# Universe size : %s' % (self.universe.locations[-1])
        print '# Max nb of iterations : %s' % (self.nb_iteration_max)
        print '#####'

    def print_launching(self):
        self.print_separator(19)
        print '>>> Launching %s ...' % (self.test_name)
        self.print_separator(19)
        print(self.universe)

    def print_nbiter_atteint(self):
        print '>>> Maximum number of iterations reached.'

    def print_separator(self, magic_number):
        """Fuck magic numbers"""
        print '#' * (magic_number + len(self.test_name))

    def print_test_successful(self):
        self.print_separator(19)
        print '>>> ...%s SUCCESSFUL.' % (self.test_name)
        self.print_separator(19)

    def print_test_failed(self):
        self.print_separator(19)
        print '>>> ...%s FAILED.' %(self.test_name)
        self.print_separator(19)
