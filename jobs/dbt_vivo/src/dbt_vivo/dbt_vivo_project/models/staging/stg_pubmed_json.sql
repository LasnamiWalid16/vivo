{{ config(materialized='view') }}

with source_pubmed_json as (
    select
        id,
        title,
        {{ format_date('date') }} as date,
        trim(journal) as journal
    from {{source('vivo','pubmed_json')}}
)

select * from source_pubmed_json
