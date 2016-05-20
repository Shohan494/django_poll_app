from django.contrib import admin
# Register your models here.
from .models import Choice, Question

# initial state
'''
admin.site.register(Question)
'''

# the state where date is before the question
'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
'''

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Final state with fieldsets
# that means each section with a field name provided
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Your Question',    {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
#just registering these to admin section
admin.site.register(Question, QuestionAdmin)
