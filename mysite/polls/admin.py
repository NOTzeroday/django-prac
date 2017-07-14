# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Question, Choice

# Register your models here.
#admin.site.register(Question)

#Customize the admin page

#class QuestionAdmin(admin.ModelAdmin):
#	fields = ['pub_date', 'question_text']

#admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3 #provide at least 3 fields for adding questions

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date Information', {'fields': ['pub_date']})
	]
	inlines = [ChoiceInline]
	list_display = ( 'question_text','pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)