{{ config(materialized='view') }}
          

WITH source_pubmed as (
    SELECT
        {{ clean_string('id') }} AS id,
        {{ clean_string('title') }} AS title,
        {{ format_date('date') }} AS date,
        {{ clean_string('journal') }} AS journal
    FROM 
        {{source('vivo','pubmed')}}
)

SELECT * FROM source_pubmed
