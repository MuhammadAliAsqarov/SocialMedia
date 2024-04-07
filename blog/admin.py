from django.contrib import admin
from .models import MyUser,Post,CommentPost,LikePost,FollowUser
admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(LikePost)
admin.site.register(FollowUser)

