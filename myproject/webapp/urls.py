from django.urls import path
from .views import ProductViewset,UserAPIView
urlpatterns=[
    path('product',ProductViewset.as_view({
        'get':'list',
        'post':'create',
    })),
    path('product/<str:pk>',ProductViewset.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    path('user',UserAPIView.as_view())
]