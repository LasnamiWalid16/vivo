## 6. Pour aller plus loin

### Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données ?

- Utilisation de **Spark** pour le traitement distribué.
- Chargement des fichiers en parallèle vers un **Cloud Storage** pour optimiser les temps d’ingestion.
- Utilisation d’une architecture **ELT** avec **DBT**, permettant de transformer les données directement dans le data warehouse.
- Mise en place de **tests automatiques** avec DBT pour assurer la fiabilité des données.
- Partitionnement, Index, Clustering des données dans BigQuery pour améliorer les performances de requêtes.

### Quelles modifications seraient nécessaires pour prendre en compte de telles volumétries ?

- Intégration d’un orchestrateur comme **Airflow** pour gérer les dépendances et l'exécution en DAG.
- Parallélisation des tasks, par example le chargement des fichiers depuis GCS en parallèle.
- Découpage des traitements en **étapes unitaires** réutilisables et testables.
- Ajout de **systèmes de monitoring et d’alerting**
- Utilisation de **formats optimisés** pour les gros volumes comme Parquet ou Avro.
