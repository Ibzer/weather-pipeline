# Weather Pipeline

Pipeline ETL qui ingere des donnees meteo horaires depuis Open-Meteo, les stocke dans PostgreSQL, les transforme avec dbt et orchestre le tout avec Airflow. Un dashboard Metabase visualise les donnees en temps reel.

## Stack

- Python 3.11
- Apache Airflow 2.9 (orchestration)
- PostgreSQL 15 (stockage)
- dbt-core + dbt-postgres (transformation et tests qualite)
- Metabase (visualisation)
- Docker + Docker Compose (conteneurisation)

## Architecture

API Open-Meteo -> fetch_weather.py -> PostgreSQL (weather_raw)
                                           |
                                 dbt stg_weather_raw (vue)
                                           |
                             dbt daily_weather_summary (table agregee)
                                           |
                                  Metabase (dashboard)

## Lancer le projet

1. Installer Docker Desktop et Python 3.11
2. Creer le venv : py -3.11 -m venv venv && venv\Scripts\activate
3. Installer dbt : pip install dbt-core dbt-postgres
4. Copier .env.example en .env et renseigner les valeurs
5. Configurer ~/.dbt/profiles.yml avec host=127.0.0.1, port=5433, dbname=airflow, user=airflow, password=airflow
6. Lancer les conteneurs : docker compose up -d
7. Activer le DAG : docker exec weather-pipeline-airflow-webserver-1 airflow dags unpause weather_pipeline
8. Lancer dbt : cd dbt_project && dbt run && dbt test

## Acces

- Airflow UI : http://localhost:8080 (airflow / airflow)
- Metabase : http://localhost:3000
- PostgreSQL : localhost:5433

## Choix techniques

dbt separe les donnees brutes des donnees transformees et integre les tests de qualite automatiques. Docker Compose garantit la reproductibilite totale de l environnement. Open-Meteo est gratuit et sans cle API. Metabase permet de visualiser les donnees sans ecrire de code supplementaire.
