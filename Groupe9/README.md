# Projet E2 : Validation de données cliniques FHIR avec SHACL

## Groupe9

| Membre | Contribution principale |
|(Antoine Vatte) | Création des règles SHACL, implémentation du `shacl_engine.py` |
| (Atangana Jeremy) | Création des données RDF mockées, script `naive_engine.py` |
| (Jules Barres) | Point d'entrée `main.py`, notebook de démo, rédaction des slides |

## Sujet

- **Identifiant du catalogue :** E2 — Valider des données cliniques FHIR avec SHACL
- **Problématique :** Les dossiers patients s'échangent au format FHIR, mais une donnée syntaxiquement correcte (JSON valide) peut être cliniquement incohérente (ex: date de décès antérieure à une naissance). Les scripts de validation codés en dur sont difficiles à maintenir à grande échelle
- **MVP :** Simulation de ressources FHIR en RDF, création d'une bibliothèque de formes SHACL structurelles et cliniques, et génération d'un rapport de validation.

## Architecture

Le projet adopte une architecture modulaire séparant les données, les règles et les moteurs d'exécution :
- `data/` : Contient le graphe de données patient mocké (`patient_invalide.ttl`) et la base de connaissances médicale (`shapes.ttl`).
- `src/generator.py` : Script générant dynamiquement 1000 patients avec un taux d'erreur clinique aléatoire (test de robustesse).
- `src/shacl_engine.py` : Module principal utilisant `pyshacl` pour valider le graphe RDF contre les règles cliniques.
- `src/naive_engine.py` : Module de comparaison contenant l'approche algorithmique classique (script en dur).
- `main.py` : Point d'entrée en ligne de commande (CLI) orchestrant la validation et mesurant les performances.
- `demo.ipynb` : Notebook interactif reprenant la logique pour la démonstration.
## Installation

```bash
# Création d'un environnement virtuel
python -m venv venv

# Installation des dépendances figées
pip install -r requirements.txt

## Utilisation

```bash
# Lancement de la validation et du comparateur
python main.py
```

## Tests

```bash
# Exécution du script principal servant de test non interactif
python main.py
```

Indiquez les résultats obtenus et les cas d'échec couverts.
Le système injecte volontairement un patient dont la date de naissance est en 1990 et la date de décès en 1985.Cas d'échec couverts : Le moteur SHACL intercepte l'aberration temporelle avec succès et renvoie un rapport d'erreur standardisé (violation de la contrainte SPARQL PatientDeathShape), empêchant l'intégration de la donnée erronée.

## Résultats et évaluation

Baseline : Notre baseline est une fonction Python classique vérifiant les dates avec des conditions if/else.

Protocole : Le script main.py chronomètre l'exécution des deux approches sur la même aberration et compare la complexité de maintenance.

Métriques et interprétation : Le script naïf s'exécute plus rapidement sur un patient unique. Cependant, l'approche SHACL prouve son énorme avantage métier : elle permet de séparer complètement la logique médicale de l'exécution. L'ajout de 500 nouvelles règles de validation se ferait uniquement en enrichissant le fichier shapes.ttl, sans avoir à modifier, retester ou recompiler le moindre script Python.

## Limites et plan B

Limites connues : Pour ce MVP, nous n'avons pas implémenté le pipeline complet de conversion JSON-LD / FHIR vers RDF, qui est complexe. Nous avons injecté des données directement modélisées en Turtle (RDF) simulant l'export d'un patient Synthea.

Dépendances externes : pyshacl et rdflib.

Plan B : En cas de défaillance matérielle lors de la soutenance, les autres membres disposeront du notebook pour le présenter

## Répartition du travail

Antoine a pris en charge la recherche sur la syntaxe SHACL/SPARQL pour formuler les contraintes médicales.

Jeremy s'est occupé de la structure des données RDF et de la baseline classique pour le comparatif.

Jules a structuré le dépôt (modularisation), géré l'intégration sur GitHub, et préparé les livrables de soutenance.Le groupe a collaboré via des sessions de travail partagées et des commits réguliers sur le dépôt distant.
## Licence et références

Code source : Distribué sous licence MIT.

Bibliothèques : rdflib et pyshacl.

https://www.w3.org/TR/shacl/

https://hl7.org/fhir/rdf.html
