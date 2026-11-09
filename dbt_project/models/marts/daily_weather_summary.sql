SELECT
    city,
    fetch_date,
    ROUND(AVG(temperature)::NUMERIC, 2)  AS avg_temp,
    MAX(temperature)                      AS max_temp,
    MIN(temperature)                      AS min_temp,
    SUM(precipitation)                    AS total_precip,
    ROUND(AVG(windspeed)::NUMERIC, 2)    AS avg_windspeed,
    COUNT(*)                              AS hours_recorded
FROM {{ ref('stg_weather_raw') }}
GROUP BY city, fetch_date
