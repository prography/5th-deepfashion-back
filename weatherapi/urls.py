from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter
from weatherapi import views

urlpatterns = [
    path('global-current/', views.get_current_weather),
    path('global-prediction/', views.get_predict_weather),
    path('domestic-current/', views.DomesticCurrentView.as_view()),
    #### ============================= legacy
    path('current-weather/', views.DomesticCurrentView.as_view()),
]

router = SimpleRouter()
urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
