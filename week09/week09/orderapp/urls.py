from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orderapp import views


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),

]