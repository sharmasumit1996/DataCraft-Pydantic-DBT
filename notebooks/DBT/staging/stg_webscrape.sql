
{{ 
    config(
        materialized='view'
        ) 
        
}}

with webscrape as(

    SELECT 
        NameOfTopic,
        Title,
        Year,
        Level,
        Introduction,
        LearningOutcome,
        LinkToPDF,
        LinkToSummary
    FROM {{ source('webscrape_data', 'cfa_courses') }}
)

SELECT * FROM webscrape