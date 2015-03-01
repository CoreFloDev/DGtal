Swig pour DGtal
===============

Versions utilisés
-----------------

Pour faire fonctionner le générateur d'interface, il faut les paquets suivants :

 * libclang-3.6-dev
 * python-clang-3.6

Le script requière l'utilisation de Python2 car la bibliothèque libclang n'est pas disponible en Python3.

Pour faire fonctionner SWIG, il faut tout d'abord être capable de compiler DGtal sur sa machine. Ensuite, il faut installer SWIG en version 3.0 (la version 3.0.2 et 3.0.5 a été utilisé pour nos tests). Ensuite, pour G++, nous avons utilisé la version 4.9.1 .

Génération d'interfaces SWIG
----------------------------

Le script python clang_swigGenerator.py permet de générer une base utilisable pour une interface 
SWIG de fichier header de DGtal.
Quelques configurations peuvent être nécéssaire pour la bonne éxécution de ce script. Les paramètres 
suceptibles d'être changés sont situé au début du fichier.

Exemple d'utilisation du script de génération d'interface :

<code><pre>./clang_swigGenerator.py src/DGtal/arithmetic/LighterSternBrocot.h
</pre></code>


Compilation d'une bibliothèque utilisable
-----------------------------------------

Il est possible de compiler une partie de DGtal avec les fichiers d'interfaces fournis

Pour compiler une interface swig, il faut :

* Générer l'interface avec SWIG.
* Compiler les parties de DGtal avec G++.
* Assembler tous les fichiers dans une bibliothèque.

Un exemple complet est disponible dans src/SWIG. Dans cet exemple, vous trouverez un fichier commande qui reprend toutes les commandes pour créer une bibliothèque.

Continuation du développement
-----------------------------

Pour améliorer le script de génération d'interface, il faudrait que le système soit capable de détecter les types déjà utilisé dans les exemples. On peut faire cela en recréant un visiteur qui parcours l'arbre avec des paramètres différents http://clang.llvm.org/docs/RAVFrontendAction.html.

Du coté de SWIG, nous avons tenté de faire fonctionner SWIG avec DGtal. Mais en modifiant SWIG, il est possible que ce soit plus simple.


