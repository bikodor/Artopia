from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
     path('', views.Home.as_view(),
          name='home'),

    path("/product/<slug:slug>/", views.ProductPage.as_view(), name='product'),

    path('/basket/', views.BasketPage.as_view(),
          name='basket'),
    path('/buy', views.SuccessBuy.as_view(),
          name='success_buy')
]