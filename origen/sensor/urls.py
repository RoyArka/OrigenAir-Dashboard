from django.urls import path, include 
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'sensor'
  
urlpatterns = [
    path('for/<slug>/', views.SensorList.as_view(), name='all'),
    path('for/<slug>/create/', views.CreateSensor.as_view(), name='create'),
    path('for/<slug>/<pk>', views.SensorDetail.as_view(), name='single'),
    path('for/<slug>/<pk>/update/', views.UpdateSensor.as_view(), name='update'),
    path('for/<slug>/<pk>/delete/', views.DeleteSensor.as_view(), name='delete'),
    path('api/for/<slug>/<pk>', views.SensorDetailAPI.as_view(), name='single-api'),
    path('api/for/<slug>/<pk>/records/<time>/<offset>', views.RecordTimeAPI.as_view(), name='time-records'),
    path('api/for/<slug>/', views.SensorListAPI.as_view(), name='sensor-list'),
    path('api/for/<slug>/<pk>/new/record/', views.NewRecordAPI.as_view(), name='new-record'),
]