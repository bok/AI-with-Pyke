# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################

# The python description of the universe.

from object import UObject
from agent import UAgent
from object_box import Box
import utils, actions
from pyke import knowledge_engine

class Universe:

    def __init__(self, size):
        """A universe is composed of agents, objects and facts which will be
        used for Pyke. For now, the locations for the universe are [0-size-1].
        The universe has a knowledge engine which is then used by the agents of the universe
        for their own cognition phase."""
        self.agents = []
        self.objects = []
        self.facts = []
        self.locations = range(size)

        # Initialization of the knowledge engine
        self.ke = knowledge_engine.engine(__file__)
        self.all_satisfied = False

        # Adding the locations of the universe in the knowledge engine
        for location in self.locations:
            self.ke.add_universal_fact('universe', 'location', (location,))

    def __str__(self):
        """A nice way of having the universe as a string for debug purposes."""
        return """
Agents : %s
Objects : %s
Facts : %s
        """ % ([a.name for a in self.agents],
               [o.name for o in self.objects],
               self.facts)

    def step(self):
        """If all the agents are not satisfied, then the universe has the non-satisfied one execute
        a step of their plan."""
        if self.all_satisfied:
            return

        aux_satisfied = True
        for a in self.agents:
            #print "GOALS (%s) -> %s" % (a.name, a.goals)
            a.step(self)


        for a in self.agents:
            aux_satisfied &= a.satisfied
        if aux_satisfied:
            self.all_satisfied = True


    def add(self, obj, location=0):
        """Adds an object or agent in the universe"""
        if location in self.locations:
            obj.location = location
        else:
            raise ValueError('Invalid location')

        # Case of an object
        if isinstance(obj, UObject):
            self.objects.append(obj)
            # Add the object to the engine as well.
            self.ke.add_universal_fact('universe', 'object', (obj.name,))

            # Case of a box
            if isinstance(obj, Box):
                self.ke.add_universal_fact('universe', 'box', (obj.name,))
                self.facts.append(('capacity', obj.name, obj.capacity))
                self.facts.append(('full', obj.name, False))
                

        # Case of an agent
        elif isinstance(obj, UAgent):
            self.agents.append(obj)
            # An agent is considered initially free (no object in his hands)
            self.facts.append(('free', obj.name, True))
            # Add the agent to the engine as well
            self.ke.add_universal_fact('universe', 'agent', (obj.name,))
            # Add the agent's capacities to the engine.
            for capacity in obj.can_do:
                self.ke.add_universal_fact('universe', 'can_do', (obj.name, capacity))
            # Add the location and free knowledge to the agent
            obj.knowledge.append(('know', obj.name, ('location', obj.name, obj.location)))
            obj.knowledge.append(('know', obj.name, ('free', obj.name, True)))

        self.facts.append(('location', obj.name, location))

    def remove(self, obj):
        """Remove an object or agent from the universe and all its related facts from the engine.
        If it is not present in the universe, raises a ValueError."""
        try:
            if type(obj) == UObject :
                self.objects.remove(obj)
            elif type(obj) == UAgent:
                self.agents.remove(obj)
        except ValueError:
            raise ValueError('No such element in the universe')

        self.remove_all_facts(obj.name)

    def remove_all_facts(self, name_obj):
        """Removes from the engine all facts related to the given name."""
        self.facts = [ (t, n, v) for (t, n, v) in self.facts
                      if n != obj.name ]

    def get(self, name_obj):
        """Returns the object or agent from the universe with the given name."""
        for e in self.objects:
            if e.name == name_obj:
                return e
        for e in self.agents:
            if e.name == name_obj:
                return e
        raise ValueError('Element not found')

    def get_fact(self, p, u):
        """Returns the fact associated to the given property and user. So if we call
        universe.get_fact('location', 'Alice') it should return (for example) ('location', 'Alice', 0)."""
        for (prop, user, value) in self.facts:
            if prop == p and user == u:
                return (prop, user, value)

    def update_facts(self, fact):
        """Updates the universe with the given fact. It tries to find a fact of same nature (property and user)
        and change its value. If there is not any fact of this kind, then it adds it."""
        utils.update(self.facts, fact)


### Actions
# These are just stubs because we want to keep the code separated for readibility purposes.
# See file actions.py .

    def move(self, name_obj, to_location):
        actions.move(self, name_obj, to_location)

    def take(self, name_agt, name_obj):
        actions.take(self, name_agt, name_obj)

    def put(self, name_agt, name_obj, to_loc):
        actions.put(self, name_agt, name_obj, to_loc)

    def give(self, name_agt, name_other, name_obj):
        actions.give(self, name_agt, name_other, name_obj)

    def place_in_box(self, name_agt, name_obj, name_box):
        actions.place_in_box(self, name_agt, name_obj, name_box)

    def fetch_from_box(self, name_agt, name_obj, name_box):
        actions.fetch_from_box(self, name_agt, name_obj, name_box)

    def order(self, name_agt1, name_agt2, add):
        actions.order(self, name_agt1, name_agt2, add)

    def ask_if(self, agent, other, situation, target):
        actions.ask_if(self, agent, other, situation, target)

    def inform_if(self, agent, other, situation, target):
        actions.inform_if(self, agent, other, situation, target)

    def ask_ref(self, agent, other, situation, target):
        actions.ask_ref(self, agent, other, situation, target)

    def inform_ref(self, agent, other, situation, target, value):
        actions.inform_ref(self, agent, other, situation, target, value)
