from django.urls import path
from .views import CafeViewSet, PassportCafeViewSet

# Cafe endpoints
cafe_list = CafeViewSet.as_view({
    'get': 'list',
})
cafe_detail = CafeViewSet.as_view({
    'get': 'retrieve',
})

# PassportCafe endpoints
passport_cafe_list = PassportCafeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
passport_cafe_detail = PassportCafeViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    # Cafes
    path('', cafe_list, name='cafe-list'),
    path('<int:pk>/', cafe_detail, name='cafe-detail'),

    # Passport Cafes
    path('passport-cafes/', passport_cafe_list, name='passport-cafe-list'),
    path('passport-cafes/<int:pk>/', passport_cafe_detail, name='passport-cafe-detail'),
]
