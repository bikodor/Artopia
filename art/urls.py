from django.urls import path
from art import views

urlpatterns = [
     path('', views.WomenHome.as_view(),
          name='home'),
path('pictures/', views.Pictures.as_view(),
          name='pictures'),

# path('games/', views.Games.as_view(),
#           name='games'),
path('bots/', views.Bots.as_view(),
          name='bots'),
path('autotests/', views.AutoTests.as_view(),
          name='autotests'),
# path('sites/', views.Sites.as_view(),
#           name='sites'),
path('leetcode/', views.LeetCode.as_view(),
          name='leetcode'),
path('QA/', views.SertificatesQA.as_view(),
          name='QA'),
# path('data_science/', views.DataScience.as_view(),
#           name='data_science'),
]

# path('music/', views.Music.as_view(),
#           name='music'),
# path('books/', views.Books.as_view(),
#           name='books'),
# path('videos/', views.Videos.as_view(),
#           name='videos'),


