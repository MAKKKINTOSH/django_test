from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["date_of_publication"], "classes": ["collapse"]})
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "date_of_publication", "was_published_recently"]
    list_filter = ["date_of_publication"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
