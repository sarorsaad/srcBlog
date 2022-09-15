
from django.urls import path
from .views import PostList,PostDetail,PostDelete,PostCreate,PostUpdate
from django.views.generic import TemplateView



urlpatterns = [
   path("", PostList.as_view(), name="post_list"),  
       
   path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
   path('index', TemplateView.as_view(template_name='index.html'), name='index'),

   path("<int:pk>/", PostDelete.as_view(), name="post_delete"),

    path("create/", PostCreate.as_view(), name="post_create"),

    path("update/<int:pk>/", PostUpdate.as_view(), name="post_Post_update"),
]

