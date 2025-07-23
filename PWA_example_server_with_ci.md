
# 📱 PWA.md – Exemple rempli (Serveur + Multi-utilisateur + CI/CD automatisé)

---

## 🔧 1. Objectif de l'application

L'application permet à deux jardiniers (moi et mon épouse) de suivre nos récoltes saisonnières, de gerer les différentes cultures, d’ajouter des photos lors de la recolte, de consulter des statistiques, de suivre les dates de semis, repiquage, plantation des différentes cultures. Les données sont sauvegardées côté serveur dans des fichiers JSON, avec possibilité d’évolution vers une base de données. Le projet intègre un système CI/CD complet pour versionnage automatique et déploiement fluide.
L'application doit être multilangue avec prise en compte du Francais et du Serbe dès la premiere version.
Nom de l'application: Baštouille
---

## 🧑‍🌾 2. Profils utilisateurs

- Jardinier 1 (moi)
- Jardinier 2 (mon épouse)
- Les informations d'un utilisateur sont persistées côté serveur ( API )
Au premier lancement de l'application, selectionner l'utilisateur dans une liste avec enregistrement de l'id dans LocalStorage. 
Les prochaines lancements, l'utilisateur est recuperer depuis LocalStorage puis appel serveur
le nom, la langue, le mode d'affichage ( clair, sombre, auto ) seront associés à l'id de l'utilisateur
---

## 📱 3. Écrans principaux

### Accueil
- Résumé des récoltes recentes
- La plus récente doit être mise en evidence 
  - l'image de culture plus grande
  - Sous l'image, la quantité et la date et l'heure
- Affichage des suivantes. Le nombre sera limité par la taille de l'écran
  - l'image de culture miniature, la quantité, la date et l'heure
### Culture
- Affichage de la liste complete des cultures ( prévoir le scroll )
  - L'image miniature, le nom
- Sur clique d'un element de la liste entrez dans un écran détail
  - lien pour revenir vers la liste
  - Image de la culture, la moitié de l'écran
  - Sous l'image, le nom
  - UUID: culture.id
  - Catégorie: culture.categorie
  - Mode de récolte: culture.moderecolte
  - Bouton "Editer"
  - Sur clique sur le bouton Editer passer l'écran en mode édition
    - Le nom, catégorie et mode de récolte passe en mode éditable
    - Le bouton "Editer" devient "Mettre à jour"
    - Sur clique sur le bouton "Mettre à jour", 
      - mettre à jour la culture côté serveur
      - afficher le message de success ou d'erreur
### Récolte ( ajout )
### Historique
### Statistiques
### Paramètres
- Accueil : résumé des récoltes récentes, mise en evidence de la plus recente et affichage des autres, dans la limite de la taille disponible à l'écran ( 2 ou 3 )
- Ajouter une récolte : formulaire de saisie avec la possibilité de prendre une photo de la recolte avec l'appareil photo + recuperation des informations meteo en lien avec la date et l'heure de la recolte
- Historique : liste de toutes les récoltes, filtrable, cumulable par culture, saison, etc..
- Statistiques : graphiques de production par mois/utilisateur/plante
- Paramètres : gestion du profil, export JSON

---

## 🧭 4. Navigation

- Barre de navigation présente sur toutes les pages
  - Accueil
  - Cultures
  - Récoltes (ajouter)
  - Historique
  - Statistiques
  - Paramètres
---

## 📦 5. Données à gérer (modèles)

### Culture
- id ( de type UUID )
- Nom 
- Image ( illustration )
- Categorie: fruit / légume / aromatique / fleur
- Mode de récolte: en poids -> gramme (ex: tomate 500g ) ou en unité ( ex: ail 3 )
  
### Récolte
- id ( uuid )
- id utilisateur
- id culture  
- quantité (nombre)
- date & heure (format DD/MM/YYYY HH:mm)
- photo (URL/base64)
- les informations méteo ( temperature, humidité, pression, vent, indice uv )

### Utilisateur
- id ( uuid )
- nom
- couleur thème (optionnel)
- langue

---

## 🔐 6. Authentification

- Pas d'authentification serveur
- Sélection manuelle de l'utilisateur sur l'app
- Association des actions à un identifiant utilisateur

---

## 🧰 7. Fonctionnalités PWA

- [x] Ajout à l’écran d’accueil
- [ ] Offline partiel (non prioritaire)
- [ ] Notifications push
- [x] Prise de photo via mobile
- [x] Synchronisation complète avec un serveur
- [x] Données stockées en JSON sur le serveur

---

## 🌐 8. Stack technique souhaitée
### 📌 Backend
- Node.js avec **Express**
- API REST exposées pour lecture/écriture de fichiers JSON (pas de base de données à ce stade)
- Serveur accessible depuis le réseau local

### 📌 Frontend
- **React** comme framework principal
- **React Router** pour la navigation multi-pages
- **Tailwind CSS** pour le style (design moderne et rapide à prototyper)
- **Vite** pour le build et le serveur de développement
### 📌 Persistance
- Persistance : fichiers JSON (`data/utilisateur1.json`), extensible vers SQLite ou PostgreSQL

---

## 🧪 9. Cas d’usage typique

1. L’utilisateur ouvre l’app depuis son iPhone
2. Il choisit “Moi” ou “Mon épouse”
3. Il clique sur “+” et prend une photo de sa récolte
4. Il entre les infos (plante, quantité, date)
5. La récolte est envoyée et stockée dans `data/mon_utilisateur.json`
6. L’autre utilisateur voit la récolte depuis son propre appareil

---

## 🔁 10. Intégration CI/CD automatisée

L’application inclut :
- Versioning automatique via `semantic-release`
- Génération automatique du `CHANGELOG.md`
- Tagging Git + création de release GitHub
- Pipeline GitHub Actions sur `main`
- Convention de commit (`feat:`, `fix:`, etc.) validée avec `commitlint` et `husky`
- Déploiement automatisé possible vers Vercel, Netlify ou un VPS

---

## 📁 11. Détail optionnel

- Export des données : bouton d’export JSON global
- Mode “invité” possible pour consultation uniquement
- Compatible iOS Safari (capture, ajout à l’écran d’accueil, offline simplifié)
