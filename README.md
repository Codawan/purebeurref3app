# Pur Beurre's Fine Food Finder App

---

## Description

L'application Fine Food Finder permet à ses utilisateurs d'accéder au descriptif complet d'un aliment choisi, et de lui trouver le substitut équivalent le plus sain. Le substitut est accompagné d'un lien vers sa fiche OpenFoodFacts et des enseignes qui le proposent à la vente.

Cette application est réalisée dans un cadre pédagogique, et constitue le projet 5 du parcours *développeur d'applications Python @ OpenClassrooms*.

## Fonctionnalités

**Du point de vue utilisateur:**

Lorsque l'utilisateur lance le programme, une fenêtre s'affiche et lui propose 2 choix:
1. *Quel aliment souhaitez-vous remplacer?*
2. *Retrouver mes aliments substitués.*

Si l'utilisateur entre "1" et en tapant *entrée*, il aura accès à un ensemble de catégories numérotées.
En tapant le numéro de la catégorie choisie puis *entrée*, il accèdera à l'ensemble des aliments de cette catégorie.
L'utilisateur devra ensuite taper le numéro de l'aliment puis *entrée*, pour avoir accès à l'aliment choisi, un substitut, sa description, un magasin où l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment. 
Enfin, le programme propose à l'utilisateur d'enregistrer le résultat dans une base de données qui liste ses recherches préférées.

**Du point de vue du développeur:**

Les fonctionnalités clés sont les suivantes:
    - L'utilisateur intéragit avec le programme dans le terminal.
    - Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme lui répète la question.
    - La recherche d'aliments se fait dans la base Open Food Facts.
    - La recherche s'effectue sur une base MySql
    - Le substitut de l'aliment choisi est celui dont l'attribut *nutriscore* est le plus élevé, pour un selection d'aliments de la même catégorie.
    - L'enregistrement des résultats de la recherche se fait dans une nouvelle table MySql.

## Licences

**Pure Beurre's Fine Food Finder** ré-utilise les données de la base de données *OpenFoodFacts* ([https://openfoodfacts.org](https://openfoodfacts.org)).
La base de données est disponible sous la licence [Open Database License](https://opendatacommons.org/licenses/odbl/1.0/).


