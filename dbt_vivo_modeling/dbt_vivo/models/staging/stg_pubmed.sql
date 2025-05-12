{{ config(materialized='view') }}
          

with source_pubmed as (
    select
        id,
        title,
        {{ format_date('date') }} as date,
        journal
    from {{source('vivo','pubmed')}}
)

select * from source_pubmed
