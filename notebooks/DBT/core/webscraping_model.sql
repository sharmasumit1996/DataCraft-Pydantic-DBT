
{{ 
    config(
        materialized='table'
        ) 
        
}}


WITH summary_web as (
SELECT
    LEVEL,
    TITLE,
    YEAR,
    COUNT(DISTINCT NAMEOFTOPIC) AS NumberOfArticles,
    MIN(LENGTH(INTRODUCTION)) AS MinLenSummary,
    MAX(LENGTH(INTRODUCTION)) AS MaxLenSummary,
    MIN(LENGTH(LEARNINGOUTCOME)) AS MinLenLearningOutcomes,
    MAX(LENGTH(LEARNINGOUTCOME)) AS MaxLenLearningOutcomes
FROM {{ source('webscrape_data', 'cfa_courses') }}
GROUP BY LEVEL,
    TITLE,
    YEAR
)

SELECT * FROM summary_web sw
ORDER BY LEVEL DESC,
        TITLE,
        sw.YEAR DESC