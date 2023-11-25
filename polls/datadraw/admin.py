from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)

class ChoiceAdmin(admin.ModelAdmin):
  list_filter = ["question"]

admin.site.register(Choice, ChoiceAdmin)