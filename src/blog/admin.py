from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm
# Register your models here.

class SitesAdmin(admin.ModelAdmin): 
	fieldsets = ( 
		(None, { 
			'fields': ('url', 'title', 'content', 'sites')
		 }),
 		 ('Advanced options', { 
 		 	'classes': ('collapse',),
  			'fields': ('registration_required', 'template_name'),
   		}), 
    )

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
# class Meta:
# 	model = SignUp

admin.site.register(SignUp, SignUpAdmin)