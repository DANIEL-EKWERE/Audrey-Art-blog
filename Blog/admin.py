from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.
#admin.site.register(myuser)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(myuser)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)
admin.site.register(AnimatedVid)
admin.site.register(PreAnimatedVid)

