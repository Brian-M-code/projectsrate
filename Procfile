web: gunicorn projectviews.wsgi --log-file -



{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    {% if title %}
        {{title}}
    {% else %}
        <title>Registration</title>
    {% endif %}

    {% block styles %}
        {% bootstrap_css %}
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    {% endblock %}
</head>
<body>
    {% include 'navbar.html' %}

    {% block content %}
    {% endblock %}

    {% block scripts %}
        <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
        {% bootstrap_javascript %}
    {% endblock %}
</body>
</html>