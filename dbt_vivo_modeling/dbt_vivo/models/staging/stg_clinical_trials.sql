with source_clinical_trials as (
    select
        id,
        scientific_title,
        {{ format_date('date') }} as date,
        trim(journal) as journal
    from {{source('vivo','clinical_trials')}}
)

select * from source_clinical_trials
