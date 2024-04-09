from django.urls import path
from .views import (home_view, upload_view, follow_view, like_view, setting_view, profile_view, profile_info_view,
                    delete_post_view,follow_profile_view,search_view,comments_view,post_authorinfo_view)

urlpatterns = [
    path('', home_view),
    path('upload/', upload_view),
    path('follow/', follow_view),
    path('like/', like_view),
    path('setting/', setting_view),
    path('profile/', profile_view),
    path('profile_info/', profile_info_view),
    path('delete_post/', delete_post_view),
    path('follow_profile/',follow_profile_view),
    path('search/',search_view),
    path('post/<int:post_id>/comments/',comments_view),
    path('post_authorinfo/', post_authorinfo_view),
    # path('sql/', sql_test_view)
]
