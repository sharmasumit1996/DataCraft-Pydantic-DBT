
{{ 
    config(
        materialized='view'
        ) 
        
}}

WITH content as (

    SELECT
        contentid,
        docid,
        level,
        year,
        title,
        article,
        LEARNINGOUTCOME
    FROM {{ source('pdf_contents','pdf_contents') }}
)

SELECT * FROM content