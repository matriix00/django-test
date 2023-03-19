from food import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('home/', views.foodIndex),
    path('foodhome/',views.findex,name="food.home"),
    path('<int:id>/',views.show,name="food.show"),
    path('delete/<int:id>',views.delete,name="food.delete"),    
    path("foodhome/create/",views.CreateFoodView.as_view(),name="food.create"),
    #4
    path("foodhome/edit/<int:pk>",views.UpdateFoodView.as_view(),name="food.update"),
    

]   