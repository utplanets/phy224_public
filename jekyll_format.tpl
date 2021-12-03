{% extends 'jekyll/index.md.j2' %}

{% block input %}
~~~
{{cell.source}}
~~~
{: .language-{%- if 'magics_language' in cell.metadata  -%}
    {{ cell.metadata.magics_language}}
{%- elif 'name' in nb.metadata.get('language_info', {}) -%}
    {{ nb.metadata.language_info.name }}
{%- endif %}}
{% endblock input %}


{% block data_text %}
~~~
{{ output.data['text/plain']}}
~~~
{: .output}
{% endblock data_text %}
