from django.contrib import admin
from .models import profile, post, Likepost, FollowersCount
# Register your models here.

admin.site.register(profile)
admin.site.register(post)
admin.site.register(Likepost)
admin.site.register(FollowersCount)

