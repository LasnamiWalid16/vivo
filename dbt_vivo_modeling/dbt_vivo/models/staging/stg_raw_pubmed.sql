WITH raw_pubmed AS (
SELECT 
    *
FROM 
    {{ref('stg_pubmed')}}

UNION ALL

SELECT 
    *
FROM 
    {{ref('stg_pubmed_json')}}
)

SELECT * FROM raw_pubmed 
ORDER BY id ASC
