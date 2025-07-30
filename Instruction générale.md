# Instruction générale

- Tu es un agent de développement web.  
- Je veux réaliser une application web avec un rendu identique à une application native iPhone. 
- L’application aura une identité visuel : un vert kaki et un couleur dorée
- Nom de l’application : Baštouille
- Nom du projet : app-bastouille
-	Next.js / React
-	Shadui / Tailwindcss
-	ESLint + Prettier
-	Données stockées en base de données postgresql. Prevoir l’installation de postgresql 
- Crées l’intégralité du projet avec l’ensemble des composants nécessaires
- Prévois un fichier readme.md qui explique tous les détails et les étapes du projet : 
installation, lancement, modification de l’identité visuel, etc, etc 
- Le projet sera géré dans VSC et avec git sur GitHub

# Fonctionnalités

## Gestion des cultures 
- ajout
- modification
- liste

### Modele culture
- id: uuid
- nom: string
- img: string ( nom du png d’illustration )
- categorie: énumération, valeurs possibles: fruit, légume, aromatique, fleur
- mode_recolte: énumération, valeur possibles: poids, poids_unite

## Gestion des recoltes
- ajout
- liste
- modification
- suppression

### Modele Recolte
- id: uuid
- id_culture: lien vers la culture récoltée
- date et heure: format DD/MM/YYYY HH:mm
- poids : le de la recolte en gramme ( pour tous les modes de recoltes
- quantite: le nombre d'unité recolté ( uniquement pour le mode de recolte poids_unite
- meteo: les données meteo réélles
	- meteo.temperature
	- meteo.humidite
	- meteo.vent
	- meteo.indice_uv
	- meteo.qte_pluie

## Visualisation des statistiques de recolte
- Voir le cumul des recoltes pour l'année selectionnée
- Comparer les récoltes d'une culture choisie par année

## Structure générale de l'application
### Zone supérieure ( barre de titre )
- Affichage du nom de l'application au centre
- En fonction de l'écran affiché, une autre information peut être affichée à la place du nom de l'application 
- En fonction de l'écran affiché, un lien de navigation pour revenir en arrière peut être affiché à gauche

### Zone centrale
- affichage du contenu d'un écran
- peut être scrollable mais uniquement entre la zone supérieure et inférieure 

### Zone inférieure dédiée à la navigation
- Accueil
- Culture
- Recolte
- Statistique

## Ecran accueil
- Aficher les dernières recoltes. 
- La toute dernière recolte est affiché en détail -> 1/3 de la zone
- Les 3 suivantes sont affichées en mode liste

## Ecran culture
- Affiche la liste des cultures disponibles
- Chaque élement de la liste: img+nom 
- Sur clique d'un élement de la liste, on rentre dans l'écran détail

### Ecran détail culture
- Affichage de toutes les données d'une culture 
- l'image s'affiche en 196x196
- Un bouton permet d'ajouter une recolte
- Possibilité de modifier le nom, la catégorie et le mode de récolte
- Si une des données est modifiée afficher un bouton mettre à jour

## Ecran Recolte
-	Choisir la culture dans une liste déroulante ( img + nom )
-	Saisie le poids en gramme 
-	Saisir le nombre d’unité ( si mode_recolte = poids_unite )
-	Affiche la date et l’heure courante avec possibilité de modifier
-	Affiche les informations méteos en temps réel recupéré depuis un site meteo
-	Bouton ajouter

## Ecran statistique
-	Afficher la liste ( liste de selection ) des années disponibles ( en fonction des recoltées réalisées )
-	Sélectionner une année
-	Afficher un tableau avec le cumul des recoltes pour l’année 
	- Col1 : img+nom de la culture
	- Col2 : poids cumulés des recoltes ( affiché en Kg )
	- Col3 : nombre d’unité pour les cultures avec mode_recolte=poids_unite


