from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter
from weather import views

urlpatterns = [
    path('domestic-current/', views.DomesticCurrentView.as_view()),
    path('global-current/', views.GlobalCurrentView.as_view()),
    path('global-prediction/', views.GlobalPredictView.as_view()),
    path('current-weather/', views.DomesticCurrentView.as_view()), # for legacy
]


router = SimpleRouter()
urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
