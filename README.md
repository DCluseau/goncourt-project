# Application de gestion du Prix Goncourt

[Contexte](#contexte)
[Objectifs de l'application](#objectifs-de-lapplication)
[Fonctionnalités principales](#fonctionnalites-principales)
[Fonctionnement](#fonctionnement)
[Pré-requis techniques](#pre-requis-techniques)

## Contexte

Le prix Goncourt 2025 a été attribué mardi 4 novembre, au restaurant Drouant à Paris, à l'issue de trois sélections successives :
 - mercredi 3/9 : première sélection comportant une liste de 15 romans ;
 - mardi 7/10 : deuxième sélection, réduite à 8 romans ;
 - mardi 28/10 : troisième sélection, révélant les 4 romans finalistes.

Chaque livre porte un titre, est décrit par un résumé, écrit par un auteur, publié par un éditeur et comporte un ou plusieurs personnages principaux. Il est également caractérisé par une date de parution, un nombre de pages, un ISBN et un prix éditeur. En outre, chaque auteur peut être décrit – de façon optionnelle – par une biographie.

Le jury est constitué par les membres de l'académie Goncourt qui est composée d'un ensemble de personnalités de l'écriture et présidée par l'une d'elles. Celui-ci établit trois sélections successives et attribut le prix Goncourt à l'auteur du roman primé à l'issue d'un dernier tour de scrutin lors duquel il obtient un certain nombre de voix, suivi par d'autres romans ayant obtenu moins de voix.

## Objectifs de l'application

L'application a pour but de permettre à un utilisateur d'afficher les livres sélectionnés pour un tour d'une année donnée. En outre, elle permet aussi au président du jury d'ajouter des livres à une sélection, ainsi que d'indiquer les votes pour chaque livre de chaque sélection.

## Fonctionnalités principales

  - Sélection d'une année et d'un tour
  - Affichage des livres d'une sélection
  - Ajout d'un livre à une sélection
  - Saisie du nombre de votes pour un livre dans une sélection
  - Attribution du prix à un livre

## Fonctionnement

Au lancement de l'application, il est demandé à l'utilisateur les informations suivantes :
  - L'année du concours
  - Le tour concerné
  - Si l'utilisateur est le président du jury

Le menu suivant s'affiche ensuite : 

   1 - Sélectionner la sélection sur laquelle travailler

   2 - Afficher les livres sélectionnés

   3 - Modifier l'année sur laquelle travailler

   0 - Quitter le programme

Si l'utilisateur est le président, un complément au menu est affiché :

   4 - Ajouter un livre à une sélection

   5 - Ajouter les votes à un livre

   6 - Indiquer quel livre a reçu le prix

Pour sélectionner une action à effectuer, il suffit de saisir le numéro du menu dans la console.
Pour chaque action, l'application affiche les informations nécessaires avant de demander à l'utilisateur de saisir une nouvelle valeur. Une fois toutes les informations acquises, l'application les traite puis retourne automatiquement au menu principal.

 - Menu 1 : 
L'application demande à l'utilisateur de saisir le numéro du tour sur lequel travailler.

 - Menu 2 : 
L'application affiche les livres sélectionnés pour l'année et le tour saisis

 - Menu 3 : 
L'application demande à l'utilisateur de saisir une année (au format AAAA)

 - Menu 0 :
Permet de quitter le programme

Pour le président du jury :

 - Menu 4 : 
L'application affiche la liste des livres enregistrés en base de données indépendamment de si ils ont été sélectionnés ou non. Elle demande ensuite à l'utilisateur d'entrer le code ISBN du livre à ajouter ainsi que le nombre de votes. Il est possible d'indiquer 0 si il n'y a pas encore eu de votes.

 - Menu 5 : 
L'application affiche les livres sélectionnés puis demande à l'utilisateur d'entrer le code ISBN du livre ainsi que le nombre de vote total.

 - Menu 6 : 
L'application affiche les livres sélectionnés pour le troisième tour de l'année puis demande à l'utilisateur de saisir l'ISBN du livre qui va recevoir le prix.

## Pré-requis techniques
- Python version 3.13
- cffi version 2.0.0
- cryptography version 46.0.3
- pycparser version 2.23
- PyMySQL version 1.1.2
- types-PyMySQL version 1.1.0.20250916
