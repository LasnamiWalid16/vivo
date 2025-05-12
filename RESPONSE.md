## 6. Pour aller plus loin

### Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données ?

- Utilisation de **Spark** ou **Dask** pour le traitement distribué.
- Chargement des fichiers en parallèle vers un **Cloud Storage** pour optimiser les temps d’ingestion.
- Utilisation d’une architecture **ELT** avec **DBT**, permettant de transformer les données directement dans le data warehouse.
- Mise en place de **tests automatiques** avec DBT pour assurer la fiabilité des données.
- Partitionnement des données dans BigQuery pour améliorer les performances de requêtes.

### Quelles modifications seraient nécessaires pour prendre en compte de telles volumétries ?

- Intégration d’un orchestrateur comme **Apache Airflow** pour gérer les dépendances et l'exécution en DAG.
- Découpage des traitements en **étapes unitaires** réutilisables et testables.
- Ajout de **systèmes de monitoring et d’alerting** (par exemple avec DataDog, Stackdriver).
- Utilisation de **formats optimisés** pour les gros volumes comme Parquet ou Avro.
- Optimisation des **requêtes SQL** et limitation des scans inutiles dans BigQuery avec des filtres efficaces.
