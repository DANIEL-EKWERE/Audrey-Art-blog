from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from Audrey_Art.settings import DEBUG , STATIC_URL , STATIC_ROOT

urlpatterns = [
    path('signup/', views.Signup,name='signup'),
  path('login/', views.Login.as_view(),name='login'),
  path('logout/',views.Logout,name='logout'),
    path('',views.home,name='home'),
   path('Post-details/<int:pk>/',views.Post_Detail,name='Post_Detail'),
   path('Search_Result/',views.Search_Result,name = 'Search_Result'),
   path('categories/<str:category>/',views.categories,name ='category'),
   path('update/<int:book_id>',views.Update ,name= 'update_post'),
   path('delete/<int:post_id>',views.Delete, name= 'delete'),
   path('Pre-Anim-vids/<str:pk>',views.PreAnimatedVideos,name='Pre_Anim_Vids'),
   path('createPost/',views.CreatePost.as_view(),name='create_post'),
   path('download/',views.download,name='download'),
   path('Video/<str:pk>',views.Video,name='video'),
   path('About/',views.About,name='about'),
]

# if DEBUG:
#   urlpatterns += static(STATIC_URL, document_root= STATIC_ROOT)