SELECT
    id,
    city,
    fetch_date,
    CAST(hour AS TIMESTAMP) AS observed_at,
    temperature,
    precipitation,
    windspeed,
    inserted_at
FROM {{ source('public', 'weather_raw') }}
WHERE temperature IS NOT NULL
