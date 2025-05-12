WITH source_drugs AS (
    SELECT
        atccode,
        drug
    FROM 
        {{source('vivo','drugs')}}
)

SELECT * FROM source_drugs 
