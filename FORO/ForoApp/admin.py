from django.contrib import admin

from ForoApp.models import User, Post, Thread, Votes

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(Votes)
