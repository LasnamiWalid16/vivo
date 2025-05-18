{% macro clean_string(column_name) %}
    case
        when {{ column_name }} is NULL then NULL
        when trim({{ column_name }}) = '' then NULL
        else trim({{ column_name }})
    end
{% endmacro %}
