README
======

AUTEURS
-------
- Florent Latombe         <florent@bokbox.com>
- Antoine Pierlot-Garcin  <antoine@bokbox.com>

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

A PROPOS DU PROJET
------------------

Ce projet consiste en la réalisation d'un système multi-agents communicants.
Les agents évoluent dans un univers, et peuvent exécuter plusieurs actions:

- Bouger d'un endroit à un autre
- Prendre un objet
- Poser un objet
- Mettre un objet dans une boîte (qui est un objet aussi)
- Sortir un objet d'une boîte
- Donner un objet ou une boîte à un autre agent
- Demander des informations à un autre agent
- Donner des informations à un autre agent

A PROPOS DE PYKE
----------------

Site officiel : http://pyke.sourceforge.net


Installation
============

- Packages nécessaires :
   * Python 2.6 ou 2.7
   * Pyke 1.1 (marche probablement avec des versions plus récentes)

- Dans le Makefile, remplacer ``PYTHON=python`` par ``PYTHON=python2`` si
   Python 3 est installé (dans Arch Linux par exemple).

- Environnement Pyke :
   Pyke doit être installé. Pyke est trouvable sur sourceforge à
   l'adresse suivante : http://sourceforge.net/projects/pyke/


Fonctionnement
==============

- Lancer les tests :
    Une série de tests basiques est disponible dans src/tests et est
    appelée grâce à ``make``. Il s'agit d'un ensemble de simulations
    basiques qui exposent différentes fonctionnalités de notre projet.

- Lancer une simulation :
    Lancer une simulation personnalisée se fait à l'aide de simulation.py. Il
    faut d'abord rentrer la simulation dans simulation.py puis l'exécuter à
    l'aide de python, par exemple ``python simulation.py``.

