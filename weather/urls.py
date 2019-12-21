from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter
from weather import views

urlpatterns = [
    path('current-weather/', views.CurrentWeatherView.as_view()),
    path('short-prediction-weather/', views.ShortPredictionWeatherView.as_view()),
]


router = SimpleRouter()
urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
