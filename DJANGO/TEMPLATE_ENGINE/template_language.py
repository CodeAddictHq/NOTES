#Template engine means the way tp write logic in Html templates
{{}} --> data
{%%} --> logic

#showing var
{{ var_name }}

#If elif (endif tag is must)
{% if condition %}
{% elif condition %}
{% else %}
{% endif %}

#for loop (used to show all data at once and endif is must)
{% for item in list %}
{{ forloop.counter }}#returns 1, 2, 3, ... counter per item
{% endfor %}


#Url return route name indicates which url should be hit from urls
{% url 'name' %}
{% url 'app_name:home' %}

#loading css (load static tag is mandetory)
{% load static %}
{% static 'path/to/file.css' %}

#add csrf_token (used in form)
{% csrf_token %}


#reduce html reduntency
{% include "file.html" %}
{% extends "base.html" %}
{% block content %}
{% endblock %}


#Showing form
{{ form.as_p }}

#showing objects specific field
{{ object.field }}


#Filtering
{{ name|upper }} #all upper only 
{{ name|lower }} #all lower only
{{ text|truncatewords:10 }} #first 10 word only += ...
{{ text|truncatexhars:10 }} #first 10 chars only += ...
