
{{ 
    config(
        materialized='table'
        ) 
        
}}

with pdf_contents as (
    SELECT * 
    FROM {{ ref('stg_pdfcontents') }}
),
pdf_metadata as(

    SELECT *
        FROM {{ ref('stg_pdfmetadata') }}
),

summary_pdf as (
SELECT
    LEVEL,
    TITLE,
    YEAR,
    COUNT(DISTINCT NAMEOFTOPIC) AS NumberOfArticles,
    MIN(LENGTH(INTRODUCTION)) AS MinLenSummary,
    MAX(LENGTH(INTRODUCTION)) AS MaxLenSummary,
    MIN(LENGTH(LEARNINGOUTCOME)) AS MinLenLearningOutcomes,
    MAX(LENGTH(LEARNINGOUTCOME)) AS MaxLenLearningOutcomes
FROM pdf_contents pc
    JOIN pdf_metadata pm
        ON pc.docid = pm.docid
GROUP BY LEVEL,
    TITLE,
    YEAR
)

SELECT * FROM summary_pdf sp
ORDER BY LEVEL DESC,
        TITLE,
        sp.YEAR DESC