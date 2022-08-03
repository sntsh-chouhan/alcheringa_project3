from django.urls import path
from.import views

urlpatterns = [
    path('index/', views.index, name='project-index'),
    path('mypost/', views.my_post, name='project-post'),
    path('logout/', views.logout_page, name='project-logout'),
    path('createnew/', views.create_new, name='project-new-post'),
    path('login/', views.login_page, name='project-login'),
    
]  