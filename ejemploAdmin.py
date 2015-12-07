from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.

class PollAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    '''
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]'''

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
