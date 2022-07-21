from django.urls import path
from . import views



urlpatterns = [
    # path('matchplayed/', views.matches_per_year),
    path('home', views.home, name = 'HOME'),
    path('register', views.register, name = 'Sign-up'),
    path('login', views.Login, name = 'Sign-in'),
    path('logout', views.Logout, name = 'Sign-out'),
    path('addpost',views.addpost, name = 'addsubreddit'),
    path('addsub',views.addsubreddit, name = 'addsubreddit'),
    path('addcomment', views.addcomment, name = 'addcomment'),
    path('post/<int:id>',views.postdetail , name = 'PostDetail'),
    path('subreddit', views.subred, name = 'Subreddit'),
    
]