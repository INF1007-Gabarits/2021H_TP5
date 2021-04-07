# TP5

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le mercredi 20 avril 2021 à 23h59](https://www.timeanddate.com/countdown/generic?iso=20200927T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif

- Renforcer la maitrise des notions de base de la lecture et l'écriture de fichiers;
- Notions de base en programmation orientée objet;
- Renforcer la maitrise des tests unitaires;
- Respecter les exigences de programmation;

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir lu le fichier [instructions.md](instructions.md) et d'avoir téléchargé le fichiers exercice.py que vous devrez compléter.
Pour ce TP, certaines contraintes sont à respecter:
- Vous ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers.
- Vous devez utiliser les surcharges d'opérateurs lorsque nécessaire!

### 1. Classe Equipe
Cette classe a comme attribut le nom, le nom de sa division et un dictionnaire représentant les statistiques de l'équipe.

Vous devez implémenter les fonction suivantes:
 #### 1.1 mettre_a_jour_stats(...)
 Cette fonction prend en paramètre un dictionnaire qui contient les éléments suivants:
  ```python
    {
        'PTS': 2,
        'BP': 5,
        'BC': 1,
        'VRP': 1
    }
 ```
 Votre but est de mettre à jour TOUTES les statistiques de l'équipe à l'aide des données de ce dictionnaire.

 #### 1.2 obtenir_attribut(...)
 Cette fonction prend en paramètre un attribut du dictionnaire représentant les statistiques de l'équipe et retourne la valeur associée à cet attribut.

 Par exemple, si l'on veut l'attribut victoire des Canadiens de Montreal, on obtiendrait 29.

 #### 1.3 Surcharge de l'opérateur ==
 La surchage doit comparer l'objet à son abbrévation. 

 Par exemple, supposons que l'on a l'objet team_mtl, qui correspond à l'équipe des Canadiens de Montreal, on voudrait que team_mtl == "MTL" retourne True.


 ### 2. Classe Division
 Cette classe a comme attribut le nom de la division et une liste des objets Equipe de la division

 Vous devez implémenter les fonction suivantes:
 #### 2.1 retirer_equipe(...)
 Cette fonction prend en paramètre une équipe. Le but de cette fonction est de supprimer l'équipe SI elle existe dans la liste des équipes.

 #### 2.2 trier_classement(...)
 Le but de cette fonction est de trier la liste des équipes de la division en fonction du nombre de points.

 #### 2.3 Surcharge de l'opérateur +=
 La surcharge doit ajouter une équipe à la liste des objets Equipe de la division

 Par exemple, si j'ai un objet représentant la division atlantique, je dois pouvoir faire division_atlantic += team_mtl

 ### 3. Classe Ligue
 Cette classe a comme attribut le nom, une liste de divisions et une liste de matchs à jouer.

Vous devez implémenter les fonction suivantes:
 #### 3.1 ajouter_division(...)
 Cette fonction prend en paramètre une division et l'ajoute à la liste des divisions

 #### 3.2 trouver_equipe_division(...)
 Cette fonction prend en paramètre une abbrévation d'un nom d'équipe et retourne l'objet représentant l'équipe et l'objet de sa division.

 #### 3.3 simulation(...)
 Fonction similaire à la fonction simulation du TP3. 
 
 Elle prend en paramètres le différentiel de l'équipe A et le différentiel de l'équipe B. 
 
 La seule différence est dans le retour de la fonction. Nous voulons qu'elle retourne que la fonction retourne les points de l'équipe A et B, le nombre de buts de l'équipe A et B, ainsi que le vrp de l'équipe A et B. La différence est que dans le TP3, on demandait uniquement le vrp de l'équipe gagnante.

 #### 3.3 mettre_a_jour_classement(...)
 Cette fonction appelle la fonction trier_classement() pour chacune des divisions de la ligue. Utilisez une boucle!

 #### 3.4 simuler_ligue(...)
 Cette fonction est très similaire à la fonction du TP3. Comme au TP3, le squelette de la fonction est donnée.

 #### 3.5 Surchage de l'opérateur +=
 La surcharge doit ajouter une partie à la liste de partie restantes

 #### 3.6 ecrire_classement(...)
 Cette fonction prends en paramètres un path et écrit le classement dans un fichier txt.

 
 ### 4. lire_classement()
Cette fonction charge en mémoire le contenu du fichier classement2019.txt et store les données dans des objets des classes Ligue, Division et Equipe.

Cette fonction retourne l'objet ligue.

 ### 5. lire_match()

 Cette fonction prend en paramètre un chemin (path) et un objet ligue. Elle a pour but de charger en mémoire le contenu du fichier matchs2019.txt et de storer les données dans l'objet ligue.

 ### 6. main
 Retirer 3 équipes de votre choix de la ligue & appeler la fonction d'écriture du classement!



