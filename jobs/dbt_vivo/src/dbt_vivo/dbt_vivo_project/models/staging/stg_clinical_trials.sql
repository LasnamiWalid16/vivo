WITH source_clinical_trials AS (
    SELECT
        {{ clean_string('id') }} AS id,
        {{ clean_string('scientific_title') }} AS scientific_title,
        {{ format_date('date') }} AS date,
        {{ clean_string('journal') }} AS journal
    FROM 
        {{source('vivo','clinical_trials')}}
)

SELECT * FROM source_clinical_trials
