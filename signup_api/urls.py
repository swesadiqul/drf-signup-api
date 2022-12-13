from api_app.views import UserViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += router.urls
