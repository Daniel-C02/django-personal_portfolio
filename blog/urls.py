from django.urls import path
from . import views

app_name = 'blog'  #set the name of your app, blog is the app name
                #this is to make sure django uses the right route for the app
                #now go to all_blogs.html
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>', views.detail, name='detail'),
]