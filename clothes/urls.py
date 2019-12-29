from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter
from clothes import views


router = SimpleRouter()
router.register(r'', views.Test)

urlpatterns = [
    path('upload/', views.ImageUploadView.as_view()),
    path('admin/', views.AdminClothingList.as_view()),
    path('<int:pk>/', views.ClothingDetail.as_view()),
    path('codilist/', views.CodiListList.as_view()),
    path('codilist/<int:pk>/', views.CodiListDetail.as_view()),
    path('myfile/', views.MyFileView.as_view()),
    # path('', views.Test.as_view()),
]

urlpatterns += router.urls



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
