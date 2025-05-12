{{ config(materialized='table') }}

WITH all_mentions AS (
    SELECT
        d.atccode,
        d.drug,
        r.id,
        r.title,
        r.date,
        r.journal,
        'pubmed' AS source
    FROM {{ ref('stg_raw_pubmed') }} r
    JOIN {{ ref('stg_drugs') }} d
        ON LOWER(r.title) LIKE CONCAT('%', LOWER(d.drug), '%')

    UNION ALL

    SELECT
        d.atccode,
        d.drug,
        c.id,
        c.scientific_title AS title,
        c.date,
        c.journal,
        'clinical_trial' AS source
    FROM {{ ref('stg_clinical_trials') }} c
    JOIN {{ ref('stg_drugs') }} d
        ON LOWER(c.scientific_title) LIKE CONCAT('%', LOWER(d.drug), '%')
)

SELECT
    atccode,
    drug,
    ARRAY_AGG(
        STRUCT(
            id,
            title,
            date,
            journal,
            source
        )
    ) AS mentions
FROM all_mentions
GROUP BY atccode, drug
ORDER BY atccode
