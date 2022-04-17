from django.contrib import admin
from .models import Question, Choice, Movie, rate

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Movie)
admin.site.register(rate)
