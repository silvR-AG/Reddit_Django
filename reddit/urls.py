from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('matchplayed/', views.matches_per_year),
    path('home', views.home, name = 'HOME'),
    path('register', views.register, name = 'Sign-up'),
    path('login', views.Login, name = 'Sign-in'),
    path('logout', views.Logout, name = 'Sign-out'),
    path('addpost',views.addpost, name = 'addsubreddit'),
    path('addsub',views.addsubreddit, name = 'addsubreddit'),
    path('post/<int:id>/comment', views.addcomment, name = 'addcomment'),
    path('post/<int:id>',views.postdetail , name = 'PostDetail'),
    path('subreddit/<int:id>', views.subred, name = 'Subreddit'),
    path('like/<int:id>', views.like_post, name = 'like_post'),
    path('unlike/<int:id>', views.unlike_post, name = 'unlike_post'),      
]