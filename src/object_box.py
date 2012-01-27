# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################

# Box are UObjects that can contain other UObjects.

from object import UObject

class Box(UObject):

    def __init__(self, name, max_capacity):
        """ Create a box with a name and a maximum capacity. The box is empty
        at start."""
        UObject.__init__(self,name)
        if max_capacity<1:
            raise ValueError('Capacity should be 1 or higher')
        else:
            self.max_capacity = max_capacity
            self.objects = []
            self.capacity = self.max_capacity

    def add(self, obj):
        """ Adds the object to the box if its capacity allows it. Returns True
        if that is the case. Else returns False."""
        if self.capacity >= 1:
            self.objects.append(obj)
            self.capacity -= 1
            return True
        else:
            return False

    def add_multiple(self, objects):
        """ Adds the list of UObjects in the box if its capacity allows it.
        In that case, returns True. If the box doesn't have the capacity
        then it returns False (and no item is added to the box)."""
        if self.capacity >= len(objects):
            self.objects.append(objects)
            self.capacity -= len(objects)
            return True
        else:
            return False

    def remove(self, obj):
        """ Removes the given UObject and returns True, unless the object was
        not in the box in the first place in which case it returns False."""
        if obj in self.objects:
            self.objects.remove(obj)
            return True
        else:
            return False

    def remove_multiple(self, objects):
        """ Goes through the passed UObjects and if it is present in the box,
        removes it from the box.
        Returns the list of removed items."""
        removed_objects = []
        for o in objects:
            if o in self.objects:
                self.objects.remove(o)
                self.capacity += 1
                removed_objects.append(o)
            else:
                pass
        return removed_objects

    def contains(self, uobject):
        """ Returns True if uobject is contained in the box."""
        if uobject in self.objects:
            return True
        else:
            return False
            
    def is_full(self):
        """ Returns True if the box is full. Else returns False."""
        if self.capacity == 0:
            return True
        else:
            return False
