{% macro format_date(date_column) %}
  CASE
    WHEN {{ date_column }} IS NULL OR {{ date_column }} = '' THEN NULL

    WHEN REGEXP_CONTAINS({{ date_column }}, r'^\d{4}-\d{2}-\d{2}$') THEN
      PARSE_DATE('%Y-%m-%d', {{ date_column }})

    WHEN REGEXP_CONTAINS({{ date_column }}, r'^\d{1,2} [A-Za-z]+ \d{4}$') THEN
      PARSE_DATE('%d %B %Y', {{ date_column }})

    WHEN REGEXP_CONTAINS({{ date_column }}, r'^\d{2}/\d{2}/\d{4}$') THEN
      PARSE_DATE('%d/%m/%Y', {{ date_column }})

    ELSE
      NULL
  END
{% endmacro %}



