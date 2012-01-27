README
======

AUTEURS
-------
 - Florent Latombe         <florent@bokbox.com>
 - Antoine Pierlot-Garcin  <bok@bokbox.com>

EXPLICATIONS
------------
 Nous avons décidé de publier ces sources afin de fournir un exemple
de programme dans le domaine de l'Intelligence Artificielle utilisant le
moteur d'inférence Pyke. En espérant que cela puisse servir aux personnes
cherchant à avoir un exemple de code Pyke pour commencer leur propre projet.

AVERTISSEMENT
-------------
  Ce projet a été réalisé dans le cadre de la dernière année d'étude
du cycle d'ingénieur en informatique et mathématiques appliquées. Il
ne fonctionne PAS totalement. Les bases sont là et fonctionnent, mais
il reste plusieurs points à améliorer pour pouvoir le faire tourner
sur des "grosses" simulations par exemple.

A PROPOS DE PYKE
----------------
 Site officiel : <http://pyke.sourceforge.net>


Installation
============

 - Packages nécessaires :
    - Python 2.6 ou 2.7
    - Pyke 1.1 (marche probablement avec des versions plus récentes)

 - Dans le Makefile, remplacer PYTHON=python par PYTHON=python2 si
    python 3 est installé (dans ArchLinux par exemple).

 - Environnement Pyke :
    Pyke doit être installé. Pyke est trouvable sur sourceforge à
    l'adresse suivante : <http://sourceforge.net/projects/pyke/>


Fonctionnement
==============

- Lancer les tests :
    Une série de tests basiques est disponible dans src/tests et est
    appelée grâce à "make". Il s'agit d'un ensemble de simulations
    basiques qui exposent différentes fonctionnalités de notre projet.

- Lancer une simulation :
    Lancer une simulation personnalisée se fait à l'aide de simulation.py. Il
    faut d'abord rentrer la simulation dans simulation.py puis l'exécuter à
    l'aide de python, par exemple "python simulation.py".

