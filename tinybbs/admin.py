from django.contrib import admin

from models import *

class TopicAdmin(admin.ModelAdmin):
    list_display  = ['title','url']
admin.site.register(Topic,TopicAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display  = ['topic','user',"created_at","content"]
admin.site.register(Post,PostAdmin)


