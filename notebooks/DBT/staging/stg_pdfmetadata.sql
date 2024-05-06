
{{ 
    config(
        materialized='view'
        ) 
        
}}

WITH metadata as (

    SELECT
        docid,
        filename,
        title,
        idno,
        level,
        year,
        textlink,
    FROM {{ source('pdf_contents','pdf_metadata') }}
)

SELECT * FROM metadata