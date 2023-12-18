
from django.urls import path
from. import views

urlpatterns =[
    path("login/", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    
    path("",views.modules, name="modules"),
    path("comments/",views.comments, name="comments"),
    path("tags/",views.tags, name="tags"),
    path("module/<str:pk>",views.module, name="module"),
    path('create-module/', views.createModule, name='create-module'),
    path('create-comment/', views.createComment, name='create-comment'),
    path('create-tag/', views.createTag, name='create-tag'),
    path('update-module/<str:pk>', views.updateModule, name='update-module'),
    path('delete-module/<str:pk>', views.deleteModule, name='delete-module'),
    path('update-comment/<str:pk>', views.updateComment, name='update-comment'),
    path('delete-comment/<str:pk>', views.deleteComment, name='delete-comment'),
    path('update-tag/<str:pk>', views.updateTag, name='update-tag'),
    path('delete-tag/<str:pk>', views.deleteTag, name='delete-tag'),
    path('register/', views.registerUser, name='register'),

]