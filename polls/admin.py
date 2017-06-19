from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Fechas', {'fields': ['pub_date']}),

        ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']



admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)