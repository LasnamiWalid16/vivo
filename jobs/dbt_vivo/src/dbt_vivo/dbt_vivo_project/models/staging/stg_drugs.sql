WITH source_drugs AS (
    SELECT
        atccode,
        trim(drug) AS drug
    FROM 
        {{source('vivo','drugs')}}
)

SELECT * FROM source_drugs 
