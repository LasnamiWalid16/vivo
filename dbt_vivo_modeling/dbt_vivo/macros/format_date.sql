{% macro format_date(date_column) %}
  CASE
    WHEN {{ date_column }} IS NULL OR {{ date_column }} = '' THEN NULL

    -- Format like '2020-01-01' (YYYY-MM-DD)
    WHEN REGEXP_CONTAINS({{ date_column }}, r'^\d{4}-\d{2}-\d{2}$') THEN
      -- Directly cast to DATE
      PARSE_DATE('%Y-%m-%d', {{ date_column }})

    -- Format like '1 January 2020' (DD Month YYYY)
    WHEN REGEXP_CONTAINS({{ date_column }}, r'^\d{1,2} [A-Za-z]+ \d{4}$') THEN
      -- Parse using 'DD Month YYYY' format
      PARSE_DATE('%d %B %Y', {{ date_column }})

    -- Format like '01/01/2019' (DD/MM/YYYY)
    WHEN REGEXP_CONTAINS({{ date_column }}, r'^\d{2}/\d{2}/\d{4}$') THEN
      -- Parse using 'DD/MM/YYYY' format
      PARSE_DATE('%d/%m/%Y', {{ date_column }})

    ELSE
      -- Return NULL if it doesn't match any known format
      NULL
  END
{% endmacro %}
