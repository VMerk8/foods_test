from django.contrib import admin
from django.urls import path, include

from foods.urls import v1_router

urlpatterns = [
    path('api/v1/', include(v1_router.urls)),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]