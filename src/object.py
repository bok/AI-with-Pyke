# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################

# Python representation of objectfs in the universe.

class UObject:

    def __init__(self, name):
        """An object in the universe has a name. Its location is
        chosen when it is added in the universe."""
        self.name = name
        self.location = None
