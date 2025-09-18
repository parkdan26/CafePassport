# cafes/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cafe, PassportCafe
from .serializers import CafeSerializer, PassportCafeSerializer

class CafeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Only list and retrieve cafes (no creation needed here)
    """
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer
    permission_classes = [AllowAny]


class PassportCafeViewSet(viewsets.ModelViewSet):
    """
    Users can add a cafe to their passport with rating/bio.
    """
    serializer_class = PassportCafeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.passport.passport_cafes.all()

    def perform_create(self, serializer):
        serializer.save(passport=self.request.user.passport)
