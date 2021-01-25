from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from orderapp import views


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)

order_cancel = views.OrderViewSet.as_view({
    'get': 'cancel',
})

order_create = views.OrderViewSet.as_view({
    'post': 'create',
})

urlpatterns = [
    path('', include(router.urls)),
    path('order/<int:pk>/cancel', order_cancel, name='order-cancel'),
    path('order/create', order_create, name='order-create'),
    path('docs',include_docs_urls(title='order')),
]