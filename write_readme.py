import pathlib

readme = pathlib.Path('README.md')
readme.write_text('''# Weather Pipeline

Pipeline ETL qui ingere des donnees meteo horaires depuis Open-Meteo, les stocke dans PostgreSQL, les transforme avec dbt et orchestre le tout avec Airflow.

## Stack

- Python 3.11
- Apache Airflow 2.9
- PostgreSQL 15
- dbt-core + dbt-postgres
- Docker + Docker Compose

## Lancer le projet

1. Installer Docker Desktop et Python 3.11
2. Creer le venv : py -3.11 -m venv venv && venv\\Scripts\\activate
3. Installer dbt : pip install dbt-core dbt-postgres
4. Configurer ~/.dbt/profiles.yml avec host=127.0.0.1, port=5433, dbname=airflow, user=airflow, password=airflow
5. Lancer les conteneurs : docker compose up -d
6. Activer le DAG : docker exec weather-pipeline-airflow-webserver-1 airflow dags unpause weather_pipeline
7. Lancer dbt : cd dbt_project && dbt run && dbt test

## Acces

- Airflow UI : http://localhost:8080 (airflow / airflow)
- PostgreSQL : localhost:5433

## Choix techniques

dbt separare les donnees brutes des donnees transformees et integre les tests de qualite. Docker Compose garantit la reproductibilite totale. Open-Meteo est gratuit et sans cle API.
''', encoding='utf-8')
print('README.md cree')
