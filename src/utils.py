# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################

# Some useful functions that we use throughout the whole program.

def remove(tuple1, tuple2):
    """Returns tuple1 without all the element in tuple2."""
    if tuple2 is None:
        return tuple1
    return tuple([e for e in tuple1 if e not in tuple2])

def union(tuple1, tuple2):
    """Returns tuple1 U tuple2"""
    if tuple1 is None:
        return tuple2
    if tuple2 is None:
        return tuple1
    l = list(tuple1)
    l.extend([e for e in tuple2 if e not in tuple1])
    return tuple(l)

def includes(tuple1, tuple2, debug=False):
    """Returns wether tuple1 contains tuple2"""
    if tuple2 is None:
        return True
    if debug:
        print '%s in %s ?' % (tuple2, tuple1)
    for e in tuple2:
        if e not in tuple1:
            return False
    return True

def replace_in(tuple1, item, rep):
    """Replaces item by rep in tuple."""
    if tuple1 is None:
        return None
    f = []
    for t in tuple1:
        e = list(t)
        for i in xrange(len(e)):
            if e[i] == item:
                e[i] = rep
        f.append(tuple(e))

    return f

def not_any(tuple1, tuple2):
    """Checks that no element of tuple2 is in tuple1"""
    if tuple2 is None:
        return True
    if tuple1 is None:
        return False
    for e in tuple2:
        if e in tuple1:
            return False
    return True

def get_facts(facts, situation, target):
    """Returns all the values of the facts matching (situation, target, value?)
    in facts"""
    return [f[2] for f in facts if (f[0], f[1]) == (situation, target)]

def update(knowledge, fact):
    """Update a knowledge list with a fact"""
    sit, tar, val = fact
    fdepth = depth(fact)

    same_depth = [e for e in knowledge if depth(e) == fdepth]
    old_facts_val = get_facts(same_depth, sit, tar)
    old_facts = [(sit, tar, of) for of in old_facts_val]

    if fdepth == 1:
        for f in old_facts:
            knowledge.remove(f)
    else:
       to_del = _update(old_facts_val, val)
       for td in to_del:
           knowledge.remove((sit, tar, td))
    knowledge.append(fact)

def _update(knowledge, fact):
    fdepth = depth(fact)
    sit, tar, val = fact
    if fdepth == 1:
        to_del = get_facts(knowledge, sit, tar)
    else:
       old_facts_val = [of[2] for of in knowledge]
       to_del = _update(old_facts_val, val)
    return [(sit, tar, td) for td in to_del]


def depth(fact):
    val = fact[2]
    depth = 1
    try:
        while len(val) == 3:
            val = val[2]
            depth += 1
    except:
        pass
    return depth
