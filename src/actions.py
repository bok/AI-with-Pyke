# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################


# Code executed when agents do actions that have consequences on the universe.

from utils import get_facts

def move(universe, name_obj, to_location):
    """Moves an agent or object from the universe to another location."""
    obj = universe.get(name_obj)
    old_loc = obj.location
    obj.location = to_location

    universe.update_facts(('location', name_obj, to_location))

    obj.update_knowledge(('location', name_obj, to_location))


def take(universe, name_agt, name_obj):
    """An agent takes an object in its hands."""
    agt = universe.get(name_agt)
    obj = universe.get(name_obj)
    old_loc = obj.location
    obj.location = name_agt

    universe.update_facts(('location', name_obj, name_agt))
    universe.update_facts(('free', name_agt, False))

    agt.update_knowledge(('location', name_obj, name_agt))
    agt.update_knowledge(('free', name_agt, False))


def put(universe, name_agt, name_obj, to_loc):
    """An agent releases an object on to the ground."""
    agt = universe.get(name_agt)
    obj = universe.get(name_obj)
    obj.location = to_loc

    universe.update_facts(('location', name_obj, to_loc))
    universe.update_facts(('free', name_agt, True))

    agt.update_knowledge(('location', name_obj, to_loc))
    agt.update_knowledge(('free', name_agt, True))


def give(universe, name_agt, name_other, name_obj):
    """An agent gives an object to another agent."""
    agt = universe.get(name_agt)
    other = universe.get(name_other)
    obj = universe.get(name_obj)

    universe.update_facts(('location', name_obj, name_other))
    universe.update_facts(('free', name_agt, True))
    universe.update_facts(('free', name_other, False))
    
    for a in (agt, other):
        a.update_knowledge(('location', name_obj, name_other))
        a.update_knowledge(('free', name_agt, True))
        a.update_knowledge(('free', name_other, False))


def place_in_box(universe, name_agt, name_obj, name_box):
    """An agent places an object in a box."""
    agt = universe.get(name_agt)
    obj = universe.get(name_obj)
    box = universe.get(name_box)

    object_was_placed = box.add(obj)
        
    old_fact = universe.get_fact('capacity', name_box)
    new_fact = ('capacity', name_box, old_fact[2] - 1)
    universe.update_facts(new_fact)
    
    if box.is_full():
        universe.update_facts(('full', name_box, True))
        agt.update_knowledge(('full', name_box, True))

    universe.update_facts(('location', name_obj, name_box))
    universe.update_facts(('free', name_agt, True))

    agt.update_knowledge(('location', name_obj, name_box))
    agt.update_knowledge(('free', name_agt, True))


def fetch_from_box(universe, name_agt, name_obj, name_box):
    """An agent fetches an object from a box."""
    agt = universe.get(name_agt)
    obj = universe.get(name_obj)
    box = universe.get(name_box)

    was_full = box.is_full()

    object_was_fetched = box.remove(obj)
    if not object_was_fetched:
        raise ValueError(('Object %s was not in the box %s') % (name_obj,
                name_box))
                            
    old_fact = universe.get_fact('capacity', name_box)
    universe.facts.remove(old_fact)
    new_fact = ('capacity', name_box, old_fact[2] + 1)
    universe.update_facts(new_fact)
    
    if was_full:
        universe.update_facts(('full', name_box, False))
        agt.update_knowledge(('full', name_box, False))

    universe.update_facts(('location', name_obj, name_agt))
    universe.update_facts(('free', name_agt, False))

    agt.update_knowledge(('location', name_obj, name_agt))
    agt.update_knowledge(('free', name_agt, False))


def order(universe, name_agt1, name_agt2, add):
    """An agent orders another agent a specific action."""
    agent = universe.get(name_agt2)
    if add:
        new_goal = [('know', name_agt2, a) for a in add]
        agent.goals.append(tuple(new_goal))
    agent.satisfied = False


def ask_if(universe, self, other, situation, target):
    """An agent asks another whether a fact is true or false."""
    them = universe.get(other)
    my_knowledge = ('know', self, ('knowif', other, (situation, target)))
    # Insert new goal in first position
    them.goals.insert(0, ('know', other, my_knowledge))
    them.satisfied = False


def inform_if(universe, agent, other, situation, target):
    """An agent responds to an ask_if."""
    me = universe.get(agent)
    them = universe.get(other)
    # Search the fact in the agent's knowledge
    knowledge = get_facts(me.knowledge, 'know', agent)
    this_fact = get_facts(knowledge, situation, target)
    if this_fact != []: 
        # I know about the fact:
        my_knowledge = ('knowif', agent, (situation, target))
        print '-+- %s informs %s that it knows about %s' \
            % (agent, other, (situation, target))
    else:
        # I don't know about the fact:
        my_knowledge = ('dontknow', agent, (situation, target))
        print '-+- %s informs %s that it doesn\'t know about %s' \
            % (agent, other, (situation, target))

    # Update knowledge of the two agents
    me.update_knowledge(('know', other, my_knowledge))
    them.update_knowledge(my_knowledge)


def ask_ref(universe, agent, other, situation, target):
    """An agent asks for the value of a fact."""
    them = universe.get(other)
    # Search the fact in their knowledge
    knowledge = get_facts(them.knowledge, 'know', other)
    values = get_facts(knowledge, situation, target)
    if len(values) != 1:
        raise(ValueError, "couldn't find the fact") 
    value = values[0]
    my_knowledge = ('know', agent, (situation, target, value))
    # Insert new goal in first position
    them.goals.insert(0, ('know', other, my_knowledge))
    them.satisfied = False


def inform_ref(universe, agent, other, situation, target, value):
    """An agent answers to an ask_ref."""
    this_fact = (situation, target, value)
    them = universe.get(other)
    me = universe.get(agent)
    # update knowledges
    them.update_knowledge(this_fact)
    me.update_knowledge(('know', other, this_fact))
