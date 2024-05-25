from django.test import TestCase

# Create your tests here.


# Template tags Part 1
# {{ }} : برای متغیر ها
# {% %} : برای سینتکس ها
# {{ x | truncatewords }} : برای تمپلیت فیلتر ها
# {{ now }} : برای نشان دادن زمان
# {{ now "Y/m/d G:i" }} 2021/10/04 10:57
# {% csrf_token %} : برای جلو گیری از حملات جعل درخواست
# {% if شرط %} موارد مشروطه  {% else %} موارد مخالف شرط {% endif %}
# {% for متغیر in کوئری ست (mitavan az reversed baraye makoos kardan estafade kard) %} مورد تکرار شونده {% endfor %}
# {{ forloop.counter }} : شمارنده حلقه را نشان میدهد
# {{ forloop.revcounter }} : شمارنده حلقه را نشان میدهد , شمارنده معکوس شده
# {% if forloop.first %} شرط اولین تکرار حلقه انجام میشود   {% endif %}
# {% if forloop.last %} شرط اخرین تکرار حلقه انجام میشود   {% endif %}
# {{ forloop.parent-loop.counter }} برای اشاره به حلقه پدر در حلقه های تو در تو استفاده میشود

# Template tags Part 2
