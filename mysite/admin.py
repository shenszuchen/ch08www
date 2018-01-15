from django.contrib import admin
from mysite import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display=('mood','nickname', 'message', 'enabled', 'pub_time')
	ordering=('-pub_time',)
admin.site.register(models.Post, PostAdmin)

class MoodAdmin(admin.ModelAdmin):
	list_display=('status',)
admin.site.register(models.Mood, MoodAdmin)
