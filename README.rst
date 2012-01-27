README
======

AUTHORS
-------

- Florent Latombe         <florent@bokbox.com>
- Antoine Pierlot-Garcin  <antoine@bokbox.com>

We're both students at INP-ENSEEIHT, Toulouse, France.

PURPOSE
-------

We decided to release these sources as an example of code in the
Artificial Intelligence field which uses the Pyke knowledge engine
feature. Hopefully, this can help other people working with Pyke
and who lack some example code.

DISCLAIMER
----------

This project was done as an assignment for computer science engineering
students in last year of the standard 5-year French engineering cycle.
It is NOT fully functionnal or working. The basics work, but there is room
for improvement and we haven't had it run on "big" situations.

ABOUT THE PROJECT
-----------------

For this project, we had to build a multi-agents system. Agents
communicate and each have their own knowledge base. They evolve in a universe,
and can execute the following actions:

- Move from one place to another
- Take an object on the floor
- Put an object down
- Put an object in a box (which is also an object)
- Fetch an object from a box
- Give an object or a box to another agent
- Ask another agent for information
- Give some information to another agent

ABOUT PYKE
----------

Official site : http://pyke.sourceforge.net


Installation
============

- Required packages :
   * Python 2.6 or 2.7
   * Pyke 1.1 (probably works with newer versions)

- In the Makefile, replace ``PYTHON=python`` with ``PYTHON=python2`` if
   python 3 is installed (in Arch Linux for example).

- Pyke environment :
   Pyke must be installed. You can find it on the sourceforge page,
   at the following address : http://sourceforge.net/projects/pyke/


Running
=======

- Run the tests :
    A series of basic tests is available in src/tests and is called
    through the ``make`` command. It is made of some basic situations to
    test the basic functionalities of the program.

- Run a simulation :
    Launching a given simulation is done in ``simulation.py`` file. The
    situation has to be entered in it and then executed with python,
    for example ``python simulation.py``.
