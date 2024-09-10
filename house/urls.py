"""
URL configuration for house project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from house_info import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.login),
    path('map_sample/', views.map_sample),
    path('word_sample/', views.word_sample),
    path('shandong/', views.city_show),
    path('city/<path:city>', views.region_show),
    path('list/<path:region_select>/', views.region_list),
    path('table_demo/', views.table_demo),
    path('detail/', views.detail_show),
    path('arima_forecast/', views.plot_arima_forecast, name='plot_arima_forecast'),

]
# urls.py
# from django.urls import path
# from .views import arima_forecast_view


