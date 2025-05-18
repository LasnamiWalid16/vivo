WITH source_drugs AS (
    SELECT
        {{ clean_string('atccode') }} AS atccode,
        {{ clean_string('drug') }} AS drug
    FROM 
        {{source('vivo','drugs')}}
)

SELECT * FROM source_drugs 
