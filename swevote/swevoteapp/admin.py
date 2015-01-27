from django.contrib import admin
from swevoteapp.models import Candidate
from swevoteapp.models import Election



class CandidateInline(admin.TabularInline):
	model = Candidate

class ElectionAdmin(admin.ModelAdmin):
	fieldsets=[
		(None,	{'fields':['position']}), 
		(None,	{'fields':['num_elected']}),
		(None, {'fields':['users_have_voted_list']}),
		('Current Election?', {'fields':['is_current']}),
	]
	
	inlines = [CandidateInline]
	list_display = ('position', 'num_elected', 'is_current')
	filter_horizontal= ('users_have_voted_list',)

admin.site.register(Candidate)
admin.site.register(Election, ElectionAdmin)