# -*- coding: utf-8 -*-

#####################################################################
# This program is free software. It comes without any warranty, to  #
# the extent permitted by applicable law. You can redistribute it   #
# and/or modify it under the terms of the Do What The Fuck You Want #
# To Public License, Version 2, as published by Sam Hocevar. See    #
# http://sam.zoy.org/wtfpl/COPYING for more details.                #
#####################################################################


from sys import path

# Runs the tests from folder src/tests/
# This is a bit messy but it should run tests which are in files testn.py with class Test in it.

# Runs test in order until one fails.
# You can reduce nb_max_tests if you want to run only the firt n tests for example.

nb_max_tests = 20
path.insert(0, './tests')

for i in range(nb_max_tests):
    module_name = 'test' + str(i)
    try:
        module = __import__(module_name)

        testclassname = 'Test'
        current_test = getattr(module, testclassname)()
        test_satisfied = current_test.run()
        if not test_satisfied:
            print '>>> Stopping test because %s failed <<<' % (module_name + '.' + testclassname)
            break

    except ImportError as e:
        #print e
        break
