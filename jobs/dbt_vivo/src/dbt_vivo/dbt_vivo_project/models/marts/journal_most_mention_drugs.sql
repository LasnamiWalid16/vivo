{{ config(
    materialized='view'  
) }}

WITH mention_count AS (
    SELECT 
        mention.journal,
        COUNT(DISTINCT r.atccode) AS total_mention_drugs
    FROM {{ ref('drug_graph') }} r,
         UNNEST(r.mentions) AS mention
    GROUP BY mention.journal
)

SELECT 
    journal,
    total_mention_drugs
FROM mention_count
WHERE total_mention_drugs = (
    SELECT MAX(total_mention_drugs) FROM mention_count
)
