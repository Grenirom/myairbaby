from django.contrib import admin
from news.models import New, Comment, Rate

admin.site.register(New)
admin.site.register(Comment)
admin.site.register(Rate)