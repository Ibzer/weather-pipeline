import requests
import psycopg2
from datetime import date

def fetch_and_insert(city: str = "Paris", lat: float = 48.8566, lon: float = 2.3522):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,windspeed_10m",
        "forecast_days": 1,
        "timezone": "Europe/Paris"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    conn = psycopg2.connect(
        host="postgres",
        dbname="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_raw (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            fetch_date DATE,
            hour VARCHAR(30),
            temperature FLOAT,
            precipitation FLOAT,
            windspeed FLOAT,
            inserted_at TIMESTAMP DEFAULT NOW()
        )
    """)

    hours = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    precip = data["hourly"]["precipitation"]
    wind = data["hourly"]["windspeed_10m"]

    for i in range(len(hours)):
        cur.execute("""
            INSERT INTO weather_raw (city, fetch_date, hour, temperature, precipitation, windspeed)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (city, date.today(), hours[i], temps[i], precip[i], wind[i]))

    conn.commit()
    cur.close()
    conn.close()
    print(f"OK — {len(hours)} lignes insérées pour {city}")

if __name__ == "__main__":
    fetch_and_insert()
